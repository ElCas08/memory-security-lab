import os
import sys


def get_process_info(pid):
    path = f"/proc/{pid}/status"

    if not os.path.exists(path):
        return None

    info = {}

    with open(path, "r") as file:
        for line in file:
            if ":" in line:
                key, value = line.split(":", 1)
                info[key.strip()] = value.strip()

    return {
        "pid": pid,
        "name": info.get("Name"),
        "memory": info.get("VmRSS"),
        "virtual_memory": info.get("VmSize"),
    }


def get_memory_maps(pid):
    path = f"/proc/{pid}/maps"

    if not os.path.exists(path):
        return []

    regions = []

    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split(None, 5)

            if len(parts) < 5:
                continue

            start, end = parts[0].split("-")

            regions.append({
                "start": int(start, 16),
                "end": int(end, 16),
                "permissions": parts[1],
                "path": parts[5] if len(parts) == 6 else "",
            })

    return regions


def read_memory(pid, start, size):
    path = f"/proc/{pid}/mem"

    try:
        with open(path, "rb") as memory:
            memory.seek(start)
            data = memory.read(size)

        return data, None

    except PermissionError as error:
        return b"", f"Permission denied: {error}"

    except OSError as error:
        return b"", f"OS error: {error}"

    except Exception as error:
        return b"", f"Unexpected error: {error}"


def search_memory(data, targets):
    findings = []

    for target in targets:
        target_bytes = target.encode()

        if target_bytes in data:
            findings.append(target)

    return findings


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python backend/analyzer.py <PID>")
        sys.exit(1)

    pid = int(sys.argv[1])

    process = get_process_info(pid)

    if process is None:
        print("Process not found.")
        sys.exit(1)

    print("PROCESS")
    print(process)

    regions = get_memory_maps(pid)

    targets = [
        "TEST_SENSITIVE_DATA_1234567890",
        "alice@example.com",
        "TEST_API_KEY_123456",
        "TEST_PASSWORD_123",
    ]

    print("\nMEMORY ACCESS TEST")

    readable_regions = 0
    successful_reads = 0
    total_bytes = 0
    findings = []

    for region in regions:

        if "r" not in region["permissions"]:
            continue

        readable_regions += 1

        size = region["end"] - region["start"]

        # Don't attempt enormous regions in this first test.
        size = min(size, 10 * 1024 * 1024)

        data, error = read_memory(
            pid,
            region["start"],
            size
        )

        if error:
            print(
                f"Could not read "
                f"{hex(region['start'])}-{hex(region['end'])}: "
                f"{error}"
            )
            continue

        successful_reads += 1
        total_bytes += len(data)

        found = search_memory(data, targets)

        for target in found:
            findings.append({
                "target": target,
                "region": region
            })

    print("\nRESULT")

    print("Readable regions:", readable_regions)
    print("Successfully read:", successful_reads)
    print("Bytes obtained:", total_bytes)

    if findings:
        print("\n⚠ SENSITIVE DATA FOUND")

        for finding in findings:
            region = finding["region"]

            print(
                f"- {finding['target']} "
                f"in {hex(region['start'])}-"
                f"{hex(region['end'])}"
            )

    else:
        print("\nNo test data found.")
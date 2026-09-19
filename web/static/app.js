document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector(
        'form[action="/test"]'
    );

    const button = document.querySelector(
        '.primary-button[type="submit"]'
    );

    if (!form || !button) {
        console.log("Sentinel: simulation form not found.");
        return;
    }

    form.addEventListener("submit", (event) => {

        event.preventDefault();

        console.log("Sentinel: simulation started.");

        startSecuritySimulation(form);

    });

});


function startSecuritySimulation(form) {

    const button = document.querySelector(
        '.primary-button[type="submit"]'
    );

    if (button) {

        button.disabled = true;

        button.innerHTML = `
            <span>SECURITY ENGINE RUNNING</span>
            <b class="button-loader"></b>
        `;

    }


    const overlay = document.createElement("div");

    overlay.className = "simulation-overlay";

    overlay.innerHTML = `

        <div class="simulation-window">

            <div class="simulation-header">

                <div>

                    <span class="simulation-kicker">
                        SENTINEL / RUNTIME ENGINE
                    </span>

                    <h3>
                        Security investigation
                    </h3>

                </div>

                <span class="simulation-live">
                    LIVE
                </span>

            </div>

            <div class="simulation-progress">

                <div
                    class="simulation-progress-bar"
                    id="simulationProgressBar"
                ></div>

            </div>


            <div class="simulation-steps">

                ${createStep(
                    "01",
                    "ACCESS",
                    "Monitoring sensitive credential access"
                )}

                ${createStep(
                    "02",
                    "BASELINE",
                    "Loading learned behavioral pattern"
                )}

                ${createStep(
                    "03",
                    "OBSERVE",
                    "Measuring credential retention"
                )}

                ${createStep(
                    "04",
                    "DETECT",
                    "Comparing current behavior with baseline"
                )}

                ${createStep(
                    "05",
                    "CLASSIFY",
                    "Determining security significance"
                )}

                ${createStep(
                    "06",
                    "REMEDIATE",
                    "Applying sensitive-data response"
                )}

                ${createStep(
                    "07",
                    "VERIFY",
                    "Confirming final security state"
                )}

            </div>


            <div class="simulation-footer">

                <span>
                    BEHAVIORAL ENGINE
                </span>

                <span id="simulationMessage">
                    Initializing...
                </span>

            </div>

        </div>

    `;


    document.body.appendChild(overlay);


    const steps = [
        "Credential access observed",
        "Baseline loaded",
        "Retention measurement active",
        "Behavioral comparison running",
        "Risk classification complete",
        "Remediation executed",
        "Security state verified"
    ];


    const progressBar =
        document.getElementById(
            "simulationProgressBar"
        );

    const message =
        document.getElementById(
            "simulationMessage"
        );


    steps.forEach((text, index) => {

        setTimeout(() => {

            const stepNumber = index + 1;

            const step =
                document.querySelector(
                    `.simulation-step[data-step="${stepNumber}"]`
                );

            if (step) {

                step.classList.add("active");

                const description =
                    step.querySelector(
                        ".step-description"
                    );

                if (description) {
                    description.textContent = text;
                }

                setTimeout(() => {

                    step.classList.remove("active");

                    step.classList.add("complete");

                    const status =
                        step.querySelector(
                            ".step-status"
                        );

                    if (status) {
                        status.textContent = "✓";
                    }

                }, 650);

            }


            if (progressBar) {

                progressBar.style.width =
                    `${(stepNumber / steps.length) * 100}%`;

            }


            if (message) {

                message.textContent = text;

            }

        }, index * 900);

    });


    /*
     * Let the visual investigation finish,
     * then actually submit the Flask form.
     */

    setTimeout(() => {

        form.submit();

    }, steps.length * 900 + 500);

}


function createStep(number, title, description) {

    return `

        <div
            class="simulation-step"
            data-step="${number.replace("0", "")}"
        >

            <span class="step-number">
                ${number}
            </span>

            <div>

                <strong>
                    ${title}
                </strong>

                <span class="step-description">
                    ${description}
                </span>

            </div>

            <b class="step-status">
                —
            </b>

        </div>

    `;

}
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

                    <p class="simulation-subtitle">
                        Sentinel is observing the sensitive-data lifecycle
                        in real time.
                    </p>

                </div>

                <span class="simulation-live">
                    ● LIVE
                </span>

            </div>


            <div class="simulation-progress">

                <div
                    class="simulation-progress-bar"
                    id="simulationProgressBar"
                ></div>

            </div>


            <div class="simulation-stage"
                 id="simulationStage">

                INITIALIZING SECURITY ENGINE

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
                    "Preparing security response"
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

        {
            message: "Credential access observed",
            stage: "OBSERVING APPLICATION ACTIVITY"
        },

        {
            message: "Behavioral baseline loaded",
            stage: "LEARNING EXPECTED BEHAVIOR"
        },

        {
            message: "Measuring credential retention",
            stage: "MONITORING SENSITIVE DATA"
        },

        {
            message: "Comparing current behavior with baseline",
            stage: "ANALYZING BEHAVIOR"
        },

        {
            message: "Risk classification complete",
            stage: "EVALUATING SECURITY RISK"
        },

        {
            message: "Security response prepared",
            stage: "RESPONDING TO DETECTED RISK"
        },

        {
            message: "Final security state verified",
            stage: "VERIFYING REMEDIATION"
        }

    ];


    const progressBar =
        document.getElementById(
            "simulationProgressBar"
        );

    const message =
        document.getElementById(
            "simulationMessage"
        );

    const stage =
        document.getElementById(
            "simulationStage"
        );


    steps.forEach((item, index) => {

        setTimeout(() => {

            const stepNumber = index + 1;

            const step =
                document.querySelector(
                    `.simulation-step[data-step="${stepNumber}"]`
                );


            /*
             * Mark previous steps complete.
             */

            document
                .querySelectorAll(".simulation-step")
                .forEach((currentStep, currentIndex) => {

                    if (currentIndex < index) {

                        currentStep.classList.remove("active");

                        currentStep.classList.add("complete");

                        const status =
                            currentStep.querySelector(
                                ".step-status"
                            );

                        if (status) {
                            status.textContent = "✓";
                        }

                    }

                });


            /*
             * Activate current step.
             */

            if (step) {

                step.classList.add("active");

                const description =
                    step.querySelector(
                        ".step-description"
                    );

                if (description) {
                    description.textContent =
                        item.message;
                }

            }


            /*
             * Update progress.
             */

            if (progressBar) {

                progressBar.style.width =
                    `${(stepNumber / steps.length) * 100}%`;

            }


            /*
             * Update main stage.
             */

            if (stage) {

                stage.classList.remove(
                    "stage-pulse"
                );

                void stage.offsetWidth;

                stage.classList.add(
                    "stage-pulse"
                );

                stage.textContent =
                    item.stage;

            }


            /*
             * Update footer message.
             */

            if (message) {

                message.textContent =
                    item.message;

            }

        }, index * 950);

    });


    /*
     * Complete the final step.
     */

    setTimeout(() => {

        document
            .querySelectorAll(".simulation-step")
            .forEach((step) => {

                step.classList.remove("active");

                step.classList.add("complete");

                const status =
                    step.querySelector(
                        ".step-status"
                    );

                if (status) {
                    status.textContent = "✓";
                }

            });


        if (stage) {

            stage.textContent =
                "SECURITY INVESTIGATION COMPLETE";

        }


        if (message) {

            message.textContent =
                "Redirecting to security results...";

        }

    }, steps.length * 950);


    /*
     * Submit to Flask after the visual
     * investigation has completed.
     */

    setTimeout(() => {

        form.submit();

    }, steps.length * 950 + 700);

}


function createStep(number, title, description) {

    return `

        <div
            class="simulation-step"
            data-step="${parseInt(number, 10)}"
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
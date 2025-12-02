# Building with AI-DLC using Amazon Q Developer

by Will Matos, Raj Jain, Siddhesh Jog, and Raja SP on 29 NOV 2025 in Amazon Machine Learning, Amazon Q, Amazon Q Developer, Artificial Intelligence, Best Practices, Developer Tools, Software Permalink  Share

The [AI-Driven Development Life Cycle (AI-DLC)](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) methodology marks a significant change in software development by strategically assigning routine tasks to AI while maintaining human oversight for critical decisions. [Amazon Q Developer](https://aws.amazon.com/q/developer/), a generative AI coding assistant, supports the entire software development lifecycle and offers the [Project Rules](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/context-project-rules.html) feature, allowing users to tailor their development practices within the platform.

Recently, [AWS made its AI-DLC workflow open-source](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/), enabling developers to create software using this methodology. This workflow is implemented in Amazon Q Developer through its Project Rules customization feature. In this post, we will demonstrate how the AI-DLC workflow operates in Amazon Q Developer using an example use case.

## AI-DLC Workflow Overview

The AI-DLC workflow is the practical implementation of the AI-DLC methodology for executing software development tasks. As outlined in the [AI-DLC Method Definition Paper](https://prod.d13rzhkk8cj2z0.amplifyapp.com/), the workflow has three phases. These phases are Inception, Construction, and Operations. Inception involves planning and architecture. Construction focuses on design and implementation. Operations cover deployment and monitoring. Each phase includes distinct stages. These stages address specific software development life cycle functions. The workflow adapts to project requirements. It analyzes requests, codebases, and complexity. This analysis determines the necessary stages. Simple bug fixes skip planning. They go directly to code generation. Complex features need requirements analysis. They also require architectural design and detailed testing.

The workflow maintains quality and control through structured milestones and transparent decision-making. At each phase, AI-DLC asks clarifying questions, creates execution plans, and waits for approval. Every decision, input, and response is logged in an audit trail for traceability. Whether building a new microservice, refactoring legacy code, or fixing a production bug, AI-DLC scales its rigor to match needs—comprehensive when complex, efficient when simple, and always in control. Figure 1 shows the phases and stages within the adaptive AI-DLC workflow. The stages shown in green boxes are mandatory, while those in yellow boxes are conditional.

![AI-DLC workflow diagram showing three phases: Inception Phase (blue) with mandatory steps for Workspace Detection, Requirements Analysis, and Workflow Planning, plus conditional steps for Reverse Engineering, User Stories, Application Design, and Units Generation; Construction Phase (green) with conditional steps for Functional Design, NFR Requirements, NFR Design, and Infrastructure Design, followed by mandatory Code Generation and Build and Test steps that loop for each unit; and Operations Phase (orange) with an Operations step. The workflow flows from User Request at the top to Complete at the bottom.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/11/24/01_AI-DLC_workflow-1.png)

Figure 1. SDLC phases and stages in AI-DLC workflow

## Prerequisites

Before we begin the walk-through, we must have an AWS account or AWS Builder Id for authenticating Amazon Q Developer. If you don’t have one, sign up for [AWS account](https://aws.amazon.com/) or [create an AWS builder id](https://docs.aws.amazon.com/signin/latest/userguide/create-builder-id.html). You can use any of the [Integrated Development Environments (IDEs) supported by Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE.html#supported-ides-features) and install the extension as per the [AWS documentation](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html). In this post, we’ll be using the [Amazon Q Developer extension in VS Code IDE](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-q-vscode). Once the plug-in is installed, you’ll need to authenticate Q Developer with the AWS cloud backend. Refer to the AWS documentation for [Q Developer authentication instructions](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-q-vscode).

The AI-DLC workflow generates various Mermaid diagrams in markdown files. To view these diagrams within your IDE, you can install a Mermaid viewer plugin.

## Let’s Begin Building!

Let’s construct a simple [River Crossing Puzzle](https://en.wikipedia.org/wiki/River_crossing_puzzle) as a web UI app using AI-DLC. By choosing a straightforward app, we can concentrate more on learning the AI-DLC workflow and less on the project’s technical intricacies.

The sections below outline the individual steps in the AI-DLC development process using Amazon Q Developer. We’ll showcase screenshots of our IDE with the Amazon Q Developer plug-in and demonstrate how to interact with the workflow.

Although we’ve used the [Amazon Q Developer IDE plug-in](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE.html) in this blog post, you can also use [Kiro Command Line Interface (CLI)](https://kiro.dev/cli/) to build with AI-DLC without any additional setup. The workflow remains the same, except that you’ll interact through the command line instead of the graphical interface in the IDE.

*As we progress through the workflow, your AI-DLC experience will be tailored to your specific problem statement. You’ll also notice the probabilistic nature of large language models (LLMs), as the questions and artifacts generated by them will vary from one run to another for the same problem statement. For example, if you attempt to replicate the same problem statement we used in this blog post, your experience will likely differ. This is expected and desirable. Despite these minor variations, we’ll eventually find a solution to the problem we initially set out to address.*

## Step 1: Clone GitHub repo containing the AI-DLC Q Developer Rules

Clone the [GitHub repo](https://github.com/awslabs/aidlc-workflows) containing the AI-DLC Q Developer Rules:

```
git clone https://github.com/awslabs/aidlc-workflows.git
```

## Step 2: Load Q Developer Rules in your project workspace

Follow the `README.md` instructions in the [GitHub repo](https://github.com/awslabs/aidlc-workflows) to copy the rules files over to your project folder.

## Step 3: Install and authenticate Amazon Q Developer Extension in IDE

Open the project folder you created in Step 2 in VS Code. Open the Amazon Q Chat Panel in the IDE and ensure that the AI-DLC workflow rules are loaded in Q Developer, as shown in Figure 2. If you don’t see what’s shown in Figure 2, please double-check the steps you performed in Step 2.

![Screenshot showing four steps to access AI-DLC rules in Amazon Q: Step 1 shows opening Amazon Q Chat Panel from the left sidebar; Step 2 shows opening a chat session in Amazon Q at the top; Step 3 shows clicking on the Rules button in the chat interface; Step 4 shows ensuring AI-DLC rules are loaded in the rules panel on the right side of the screen.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/11/24/02_AI-DLC_Rules-1.png)

Figure 2: AI-DLC rules enabling in Amazon Q Developer

## Step 4: Start the AI-DLC workflow by entering a high-level problem statement

Our development environment is now set up, and we’re ready to begin application development using AI-DLC. In our Q Developer chat session, we enter the following problem statement:

```
Using AI-DLC let's build a web application to solve the river crossing puzzle.
```

Notice that we’ve prefixed our problem statement with “Using AI-DLC …” to ensure that Q Developer engages the AI-DLC workflow. Figure 3 shows what happens next. The AI-DLC workflow is triggered within Q Developer. It greets us with a welcome message and provides a brief overview of the AI-DLC methodology.

Figure 3 shows an expanded view of the AI-DLC workflow rules folder structure on the left. You’ll notice that a single `aws-aidlc-rules/core-workflow.md` is placed in the [designated](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/context-project-rules.html) `.amazonq/rules` folder, while the rest of the rules files are placed in an ordinary `aws-aidlc-rule-details` folder. This arrangement is designed to optimize model efficiency. By placing the `aws-aidlc-rules/core-workflow.md` file in the `.amazonq/rules` folder, , it serves as additional context, ensuring that the core workflow structure is always accessible without incurring additional token consumption. Conversely, the detailed phase and stage-level behavior rules are stored in the `aws-aidlc-rule-details` folder and are dynamically loaded as required. This approach conserves Amazon Q’s context window and token usage by retaining only the necessary information within the context at any given time, thereby enhancing model efficiency.

The rules files under the `aws-aidlc-rule-details` folder are organized into three sub-folders, each representing a phase of AI-DLC. Within each phase, there are stage-specific files. A `common` folder houses cross-cutting rules applicable to all AI-DLC phases and stages such as the “human-in-the-loop”.

The AI-DLC workflow is self-guided and provides us with a clear understanding of what to expect next. It informs us that it will enter the AI-DLC Inception phase next, starting with the Workspace Detection stage within it.

![Screenshot of Amazon Q interface showing AI-DLC workflow initialization. The left sidebar displays a file tree with various workflow stages and configuration files. The main chat area shows a problem statement input box at the top with placeholder text 'Using AI-DLC let's build a web application to solve the most pressing problem.' Below is a welcome message explaining AI-DLC (AI-Driven Development Life Cycle) and its capabilities. Three callout annotations highlight: 1) The core workflow dynamically utilizes detailed instructions for different phases and stages, loading and unloading them as required; 2) AI-DLC workflow kicks off with a welcome message and precise overview; 3) The workflow is structured to load a single Q Developer Rule file, one workflow.md, which then dynamically loads and unloads the stage definitions housed in the 'aws-aidlc-rule-details' folder as needed.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/11/24/03_AI-DLC_problem_statement-1.png)

Figure 3: User enters high level problem statement in Amazon Q. AI-DLC workflow is triggered.

## Step 5: Workspace Detection

We enter the **Workspace Detection** stage within the **Inception** phase. In this stage, AI-DLC analyzes the current workspace and determines whether it’s a greenfield (new) or brownfield (existing) application. Since AI-DLC is an adaptive workflow, it decides whether the next stage will be Reverse Engineering (for brownfield projects) or Requirements Analysis (for greenfield projects).

Since we’re building a greenfield application and there’s no existing code in the workspace to reverse engineer, the workflow will guide us to Requirements Analysis next. If we were working on a brownfield application, the workflow would have performed Reverse Engineering first and then moved on to Requirements Analysis. This demonstrates the adaptive nature of the workflow.

Figure 4 illustrates the process in our IDE when we enter this stage. The workflow requests our permission to create an `aidlc-docs` folder under the project root. This folder will serve as the repository for all the artifacts generated by AI-DLC during the workflow execution. Subsequently, the workflow generates two files within this folder: `aidlc-state.md` and `audit.md`. The purpose of these files is explained in Figure 4.

![Screenshot of AI-DLC workspace detection phase showing the Amazon Q chat interface. The left sidebar displays the file tree with an 'aidlc-doc' folder highlighted. The main chat area shows the Inception Phase - Workspace Detection stage with explanatory text about analyzing the workspace. Five callout annotations explain: 1) Workflow creates aidlc-doc directory for storing AI-DLC generated artifacts; 2) The workflow tracks its progress in aidlc-metadata.json for error recovery and session continuity; 3) The audit.md file stores user's prompts; 4) Workflow highlights the AI-DLC phase and stage name with a clear heading for easy tracking; 5) Workflow loads detailed stage-level behavior files dynamically such that they don't consume the context window statically. At the bottom, a user approval prompt shows 'mkdir -p /Users/[...]/NewConsumerPortal/aidlc-docs' with the user asked to approve the 'mkdir' command.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/11/24/04_AI-DLC_workspace_detection-1.png)

Figure 4: Workspace Detection

The Workspace Detection will quickly finish as this is a greenfield project. The workflow will guide us into Requirements Analysis stage within the Inception phase next.

## Step 6: Requirements Analysis

The workflow has progressed to the Requirements Analysis stage, where we will define the application requirements. The AI-DLC workflow presented our high-level problem statement to the Q Developer, which then responded with several requirements clarifications questions, as illustrated in Figure 4.

Several AI-DLC rules came into play at this stage. One rule instructed Amazon Q to avoid making assumptions on the user’s behalf and instead ask clarifying questions. Since LLMs tend to make assumptions and rush towards outcomes, they must be explicitly instructed to align with the engineering rigor of the AI-DLC methodology. To achieve this, the Q Developer presented several requirements clarification questions in `requirement-verification-questions.md` file and asked us to answer them inline in the file.

Another AI-DLC rule instructed the Q Developer to present questions in multiple-choice format and always include an open-ended option (“Other”) to enhance user convenience and provide flexibility in answering.

As shown in Figure 5, Amazon Q has asked us about the desired puzzle variant, such as the Classic Farmer, Fox, Chicken, and Grain puzzle or other popular variations. Additionally, it has asked us questions about user interaction methods, score persistence across multiple players, and the creation of a leaderboard.

These questions are essential for achieving our desired application outcome. Our responses to these questions will determine the final product. While we didn’t explicitly specify this level of detail in our high-level problem statement, AI-DLC has delegated detailed requirements elaboration to Amazon Q, but we still retain control over what gets built.

![Screenshot of AI-DLC Requirements Analysis phase showing a split view. The left side displays a requirements clarification questions markdown file with multiple-choice questions about the Kuer Crossing Portal, including sections about user crossing portal variants, primary user interaction methods, and data storage preferences. The right side shows the Amazon Q chat interface with the Inception Phase - Requirements Analysis heading. Two callout annotations highlight: 1) AI-DLC asks questions in multiple choice format, with an 'Other' option that leaves an open-ended fill-in-the-blank when the answer doesn't match the predefined options; 2) AI-DLC generates config.requirements-clarification-questions.md file containing requirements clarification questions, with questions placed in an MD file where the user can respond inline in the file, using 'Answered' to indicate completion. The chat shows instructions for answering questions to clarify requirements.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/11/24/05_AI-DLC_requirements_analysis-1.png)

Figure 5: Requirements Analysis

We answer all the questions in `requirement-verification-questions.md` file and enter “Done” in the chat window.

Amazon Q processes our responses. The AI-DLC workflow is designed to identify human errors. It checks if we’ve answered all the questions and identifies any contradictions or ambiguities in our answers. Any confusions, contradictions, or ambiguities will be flagged for follow-up questions. AI-DLC adheres to high standards and ensures that we don’t proceed to the next step until we’re fully in agreement on the requirements between us and Amazon Q.

Since we answered all the questions and there were no contradictions in our answers, the workflow continues and generates a comprehensive `requirements.md` document, as shown in figure 6.

![Screenshot showing AI-DLC requirements review phase with split view. The left side displays a Requirements Document for the River Crossing Puzzle Web Application, including Intent Analysis Summary, User Request details, Request Type, and Functional Requirements with Core Puzzle Functionality items (FR-001 through FR -006) describing game features like classic farmer puzzle, timer display, move tracking, puzzle state validation, and victory messages. The right side shows the Amazon Q chat interface with 'Requirements Analysis Complete' heading, displaying project details including Puzzle Type (Classic Farmer, Fox, Chicken, and Grain river crossing puzzle), Technology (React-based modern web application), and Target Devices (web browsers only). Three callout annotations highlight: 1) Requirements Analysis phase complete; 2) Requirements document generated; 3) User may Request Changes, Add User Stories for Approval, or Approve & Continue, with a REVIEW SAFETY note warning users to review requirements and approve to continue, with options to request changes or add modifications if required.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/11/24/06_AI-DLC_requirements_review-1.png)

Figure 6: Requirements Review

The workflow prompts us to review the `requirements.md` document and decide on the next step. If we’re not aligned on the requirements, we can prompt Amazon Q to help us achieve alignment. We can then iterate on the requirements until we’re fully aligned. Once we’re fully aligned, we prompt AI-DLC to progress to the next stage.

Given the adaptive nature of the AI-DLC workflow, Amazon Q has recommended that this application is simple enough, and we can skip the User Stories stage. If we felt otherwise, we would have overridden the model’s recommendation. In this case, we agree with Q’s recommendation and will therefore enter “Continue” in the chat window.

The workflow will enter Workflow Planning stage next.

## Step 7: Workflow Planning

With our requirements established, we proceed to the Workflow Planning stage. In this phase, we leverage the requirements context and the workflow’s intelligence to plan the execution of specific stages of AI-DLC within the workflow to build our application as per the requirements specification.

Figure 7 illustrates the workflow planning stage in Q Developer. The workflow has generated an `execution-plan.md` file that outlines the recommended stages for execution and those that should be skipped.

The workflow planning process is highly contextual to the requirements. During requirements analysis, we decided to develop a simple river crossing puzzle application, consisting of a single HTML file, without a backend, leaderboard, or persistence. Consequently, Amazon Q recommends that we skip all the conditional stages, such as User Stories, Application Design, Units of Work Planning, and so on, and proceed directly to the Code Generation Planning stage in the Construction phase.

Figure 7 visually represents the recommended workflow graphically, indicating the stages that will be executed and those that will be skipped.

![Screenshot of AI-DLC Workflow Planning phase showing an Execution Plan document on the left with Detailed Analysis Summary including user-facing changes, brownfield changes, API changes, and NFR changes, plus Risk Assessment. Below is a Workflow Visualization flowchart diagram showing the workflow stages from Inception through Construction to Operations phases. The right side shows the Amazon Q chat with 'Workflow Planning Complete' heading. Three callout annotations highlight: 1) AI -DLC workflow has analyzed requirements and based on the problem complexity has proposed a set of stages to execute in the workflow; 2) Problem is simple enough that AI-DLC is proposing to skip the detailed optional stages; 3) User may Request Changes, Add back skipped stages or Approve & Continue.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/11/24/07_AI-DLC_workflow_planning-1.png)

Figure 7: Workflow Planning

Since we’ve opted for a straightforward web UI app in this blog post for brevity, the workflow execution plan suggested by AI-DLC aligns seamlessly with our objectives. Should we not be aligned with the AI-DLC recommended workflow execution plan, we would request Q Developer to modify the plan to suit our preferences.

Since we’ve agreed on the workflow plan, we’ll enter “Continue” in Q’s chat session. If we weren’t aligned with the recommended workflow execution plan, we’d have prompted Q with our concerns and iterated over the revised execution plan until it aligned with our preferences. Following the recommended execution plan, the workflow will transition into the Construction phase and directly into the Code Generation Plan stage in the phase.

## Step 8: Code Generation Planning

AI-DLC prioritizes planning over rushing to outcomes. This approach aligns with the concept of human-in-the-loop behavior, allowing us to detect issues early on, provide feedback on the plan, and prevent wrong assumptions from propagating further. Before we proceed with actual Code Generation, we undergo Code Generation Planning.

During Code Generation Planning, AI-DLC creates a detailed, numbered plan. It analyzes the requirements and design artifacts, breaking down the process into explicit steps for generating business logic, the API layer, the data layer, tests, documentation, and deployment files.

The plan is documented in a `{unit-name}-code-generation-plan.md` file, complete with check boxes. This ensures transparency, allowing users to see what will be built. It also provides control, enabling users to modify the plan. Additionally, it maintains quality by ensuring comprehensive coverage of code, tests, and documentation.

Figure 8 illustrates the AI-DLC’s code generation plan. The proposed workflow comprises eight steps, starting with creating an HTML structure and progressing to adding styling, game logic, and concluding with testing and documentation.

![Screenshot of AI-DLC Code Generation Planning showing a Code Generation Plan document for River Crossing Puzzle on the left, with Unit Context listing HTML Structure, CSS Styling, and JavaScript files, followed by Unit Generation Steps including Step 1: HTML Structure Generation, Step 2: CSS Styling Generation, and Step 3 : Core Game Logic Generation with detailed checkboxes for each step. The right side shows Amazon Q chat with code generation plan details. Three callout annotations highlight: 1) The plan doc contains to-do items for AI-DLC to execute. These checkboxes get completed when the task is done; 2) This is how AI-DLC workflow persists and tracks progress state; 3) AI-DLC has proposed an 8-step code generation plan with checkboxes and review prompts, and User may Request Changes or Approve & Continue.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/11/24/08_AI-DLC_code_gen_planning-1.png)

Figure 8: Code Generation Planning

The code generation plan appears reasonable to us. We will proceed to the Code Generation stage by entering “Continue” in Q’s chat session.

## Step 9: Code Generation

The Code Generation stage executes the Code Generation Plan we approved in the previous step. It generates actual code artifacts step-by-step, including business logic, APIs, data layers, tests, and documentation. Completed steps are marked with check boxes, progress is tracked, and story traceability is ensured before presenting the generated code for user approval.

Figure 9 illustrates that the Code Generation stage has been completed. We are now reviewing a single `index.html` file generated with embedded styling and JavaScript consistent with our preference specified in `requirements.md`.

The workflow provides a summary of the activities performed during the Code Generation phase.

![Screenshot of AI-DLC Code Generation phase showing generated HTML code on the left with embedded styling and JavaScript for the River Crossing Puzzle application. The right side shows Amazon Q chat with 'Code Generation Complete - river-crossing-puzzle' heading and a list of generated artifacts including HTML file, CSS interface, drag-and-drop interface, game logic, and testing services. Two callout annotations highlight: 1) The generated code is an HTML file with embedded styling and JavaScript; 2) We have specified during requirements analysis phase that we want a single-file index.html file implementation; 3) Code generation has been completed, and a summary of the generated artifacts is provided.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/11/24/09_AI-DLC_code_generation-1.png)

Figure 9: Code Generation

We’re about to test our newly created application soon. While it may be straightforward to test this simple puzzle app right now, for complex applications, we generate build and test instructions using AI-DLC.

We’ll enter “Continue” in the workflow and enter the final Build and Test stage in the Construction phase.

## Step 10: Build and Test

These questions are essential for achieving our desired application.

We’ve reached the final stage of the AI-DLC Construction Phase, known as the Build and Test stage. During this stage, we create comprehensive instruction files that guide the build and packaging of the project, and document the necessary testing layers. These layers include unit tests (validating generated code), integration tests (checking unit interactions), performance tests (load/stress testing), and additional tests as required (security, contract, e2e).

The generated build instructions include dependencies and commands, test execution steps with expected results, and a summary document that provides an overview of the overall build/test status and the project’s readiness for deployment.

Figure 10 illustrates the documentation generated during this stage.

![Screenshot of AI-DLC Build and Test phase showing a Build and Test Summary document on the left with Build Status (Build Tool, Build Status, Build Artifacts, Build Warnings) and Test Execution Summary including Unit Tests, Integration Tests, and Performance Tests sections with checkmarks and failure indicators. The right side shows Amazon Q chat with build and test completion status and project summary. Two callout annotations highlight: 1) Build and Test Complete! Build and Test instructions have been documented; 2) The AI-DLC workflow has concluded with a comprehensive summary of all completed stages and generated artifacts.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/11/24/10_AI-DLC_build_and_test-2.png)

Figure 10: Build and Test

The AI-DLC workflow has now concluded.

## Let’s Solve the Puzzle!

We open `index.html` in a web browser to access our newly created River Crossing Puzzle application. As shown in figure 11, we see our graphical web UI.

During requirements assessment, we chose a straightforward user interface using HTML, CSS, and JavaScript (without any frameworks), as evident in the display shown in Figure 11. Your display may vary due to the probabilistic nature of LLMs and the choices you made for requirements.

We attempt to solve the puzzle and find that it works as expected.

![Side-by-side screenshots of the River Crossing Puzzle web application showing two game states. The left screenshot shows the initial state with a farmer on the left bank, and fox, chicken, and grain items listed below, with a blue river in the center and right bank on the right. The right screenshot shows a game state after moves with the farmer on the right bank and a success message 'Congratulations! You won in 7 moves!' displayed at the bottom. Both screens have a yellow 'Start Over' button and show move counts.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/11/24/11_AI-DLC_river_crossing_app-1.png)

Figure 11: River Crossing Puzzle Web App

## Conclusion

This post shows how AWS’s open-source AI-DLC workflow, guided by Amazon Q Developer’s Project Rules feature, helps developers build applications with structured oversight and transparency.

Using a River Crossing Puzzle web application as an example, the walk-through illustrates how AI-DLC methodology adapts its rigor based on project complexity, skipping unnecessary stages for simple applications while maintaining comprehensive processes for complex projects. Throughout each stage, AI-DLC enforces “human-in-the-loop” behavior, requiring user approval at critical checkpoints, asking clarifying questions, and maintaining complete audit trails for traceability.

The exercise successfully demonstrates how AI-DLC balances AI automation with human oversight, enhancing productivity without sacrificing quality or control. By following this structured, repeatable methodology, development teams can leverage generative AI’s capabilities while ensuring humans remain in charge of architectural decisions and implementation approaches. This framework provides the necessary guardrails for responsible and effective AI-assisted software development across projects of varying complexity.

## Cleanup

We did not create any AWS resources in this walk-through, so no AWS cleanup is needed. You may cleanup your project workspace at your discretion.

**Ready to get started?** Visit our [GitHub repository](https://github.com/awslabs/aidlc-workflows) to download the AI-DLC workflow and join the [AI-Native Builders Community](https://ai-nativebuilders.org/) to contribute to the future of software development.

About the authors:

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/11/28/RajaProfile.jpeg)

### Raja SP

Raja is a Principal Solutions Architect at AWS, where he leads Developer Transformation Programs. He has worked with more than 100 large customers, helping them design and deliver mission critical systems built on modern architectures, platform engineering practices, and Amazon inspired operating models. As generative AI reshapes the software development landscape, Raja and his team created the AI Driven Development Lifecycle (AI-DLC) — an end to end, AI native methodology that re-imagines how large teams collaboratively build production-grade software in the AI era.

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/11/28/raj.png)

### Raj Jain

Raj is a Senior Solutions Architect, Developer Specialist at AWS. Prior to this role, Raj worked as a Senior Software Development Engineer at Amazon, where he helped build the security infrastructure underlying the Amazon platform. Raj is a published author in the Bell Labs Technical Journal, and has also authored IETF standards, AWS Security blogs, and holds twelve patents

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/11/28/image-11.jpg)

### Siddhesh Jog

Siddhesh is a Senior Solutions Architect at AWS. He has worked in multiple industries in a wide variety of roles and is passionate about all things technology. At AWS Siddhesh is most excited to help customers transition to the AI Driven Development Lifecycle and enable them to build applications rapidly in a secure, complaint and cost efficient cloud environment.

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2024/06/28/wilmatos.jpeg)

### Will Matos

Will Matos is a Principal Specialist Solutions Architect with AWS’s Next Generation Developer Experience (NGDE) team, revolutionizing developer productivity through Generative AI, AI-powered chat interfaces, and code generation. With 27 years of technology, AI, and software development experience, he collaborates with product teams and customers to create intelligent solutions that streamline workflows and accelerate software development cycles. A thought leader engaging early adopters, Will bridges innovation and real-world needs .
# Anthropic Prompt Ladder: Summarizing Advanced ML Research Papers

**Task Source:** FL-01 Workflow Audit (Target Task 3: Summarizing Advanced ML Research Papers for PyTorch Implementation)
**Specific Task:** Summarizing the methodology of "LoRA: Low-Rank Adaptation of Large Language Models" (Hu et al., 2021) to implement the matrix initialization in PyTorch.

---

## The Baseline
**Prompt:** "Summarize this ML research paper. [Pasted text of the LoRA paper]"

**Output Excerpt:**
*"This paper introduces Low-Rank Adaptation (LoRA), a new method for fine-tuning large language models like GPT-3. Instead of updating all the model's weights, LoRA freezes the pre-trained weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture. This significantly reduces the number of trainable parameters..."*

**Notes:**
- **What changed:** (Baseline)
- **What improved:** N/A. 
- **What failed:** It just gave me a high-level conceptual summary. It reads like a blog post. It gave me zero mathematical insights on how to actually code the algorithm or the shapes of the decomposition matrices.

---

## Version 1: Role Assignment
**Prompt:** "Act as an elite AI researcher mentoring a junior engineer. Summarize this ML research paper. [Pasted text of the LoRA paper]"

**Output Excerpt:**
*"Let's break down the architecture of LoRA for your implementation. The authors tackle the computational bottleneck of fine-tuning by introducing a low-rank approximation. For a pre-trained weight matrix W0, they constrain the update by representing it as a low-rank decomposition..."*

**Notes:**
- **What changed:** Added **Role Assignment** ("elite AI researcher mentoring a junior").
- **What improved:** The tone instantly shifted. It stopped using marketing speak and adopted a direct, technical vocabulary, immediately mentioning the weight matrix `W0` and low-rank approximation.
- **What failed:** It was still a massive wall of text that summarized the entire paper, including the irrelevant "Empirical Experiments on RoBERTa" section.

---

## Version 2: Context and Motivation
**Prompt:** "Act as an elite AI researcher mentoring a junior engineer. Summarize this ML research paper. I am asking because I need to implement this specific algorithm in PyTorch today, and I only care about the core mathematics. [Pasted text of the LoRA paper]"

**Output Excerpt:**
*"Skipping the theoretical background, the core algorithm relies on modifying the forward pass. The primary equation you need to implement is `h = W_0 x + \Delta W x = W_0 x + B A x`. Here, `W_0` is the frozen pre-trained weight..."*

**Notes:**
- **What changed:** Added **Context and Motivation** (implementing in PyTorch today).
- **What improved:** The AI completely ignored the introductory and experiment sections of the paper, saving me from reading paragraphs of useless context. It jumped straight to the forward pass equation.
- **What failed:** It gave me the equation, but it explained it like I was a beginner who didn't know what a forward pass was, which wasted space.

---

## Version 3: Few-Shot Examples
**Prompt:** "Act as an elite AI researcher mentoring a junior engineer. Summarize this ML research paper. I am asking because I need to implement this specific algorithm in PyTorch today, and I only care about the core mathematics. Example of what I want: Do not define fine-tuning; instead, tell me exactly how matrices A and B are initialized and multiplied. [Pasted text of the LoRA paper]"

**Output Excerpt:**
*"Matrix A is initialized using a random Gaussian distribution (`torch.randn`), while Matrix B is initialized with zeros (`torch.zeros`). This ensures that `\Delta W = BA` is zero at the beginning of training. They are then scaled by `\alpha / r` before being added to the main output..."*

**Notes:**
- **What changed:** Added a **Few-Shot Example** (the matrix initialization).
- **What improved:** It completely dropped basic ML definitions and instantly provided the exact PyTorch initialization logic required for my code.
- **What failed (The "This didn't help" moment):** The output became a chaotic brain-dump of math. It was highly accurate, but impossible to skim because the tensor shapes were buried inside thick paragraphs. It was technically dense but structurally a mess.

---

## Version 4: Output Structure
**Prompt:** "Act as an elite AI researcher mentoring a junior engineer. Summarize this ML research paper. I am asking because I need to implement this specific algorithm in PyTorch today, and I only care about the core mathematics. Example of what I want: Do not define fine-tuning; instead, tell me exactly how matrices A and B are initialized. 
Output your summary strictly in this format:
1. The Core Equation
2. Tensor Shapes
3. Implementation Gotchas
[Pasted text of the LoRA paper]"

**Output Excerpt:**
*"### 1. The Core Equation
`h = W_0 x + \Delta W x = W_0 x + B A x`

### 2. Tensor Shapes
- `W_0`: `[d, k]`
- `B`: `[d, r]`
- `A`: `[r, k]`

### 3. Implementation Gotchas
- Ensure you apply the scaling factor `\alpha / r` to `\Delta W`, otherwise the learning rate will need aggressive retuning..."*

**Notes:**
- **What changed:** Added **Output Structure**.
- **What improved:** The chaotic math was perfectly organized into three highly scannable headers. I can now look directly at "Tensor Shapes" while writing my code.
- **What failed:** In the "Gotchas" section, the AI occasionally hallucinated minor tensor dimension mismatches because it rushed to format the output instead of reading the paper carefully.

---

## Version 5: Step Decomposition
**Prompt:** "Act as an elite AI researcher mentoring a junior engineer. Summarize this ML research paper. I am asking because I need to implement this specific algorithm in PyTorch today, and I only care about the core mathematics. Example of what I want: Do not define fine-tuning; instead, tell me exactly how matrices A and B are initialized. 
Before outputting, use a \`<scratchpad>\` block to identify exactly which equations are required for implementation and verify their tensor dimensions.
Then, output your summary strictly in this format:
1. The Core Equation
2. Tensor Shapes
3. Implementation Gotchas
[Pasted text of the LoRA paper]"

**Output Excerpt:**
*"\`<scratchpad>\`
Scanning methodology... The paper defines the forward pass in Eq 3. The tensor shape for W_0 is d x k. B is d x r, and A is r x k. When multiplied, BA results in d x k, matching W_0. I need to highlight the \alpha / r scaling factor in the gotchas.
\`</scratchpad>\`

### 1. The Core Equation..."*

**Notes:**
- **What changed:** Added **Step Decomposition** (\`<scratchpad>\`).
- **What improved:** Accuracy skyrocketed. By forcing the AI to think step-by-step and mathematically verify the `d x k` dimensions *before* generating the formatted output, hallucinations dropped to zero.

---

## Cross-Model Comparison (Claude vs. ChatGPT)
I ran the exact final prompt (Version 5) on the LoRA paper through both Claude 3.5 Sonnet and ChatGPT (GPT-4o).
- **Tone & Structure:** Claude adhered perfectly to the requested structure and kept the tone strictly academic and precise. ChatGPT ignored the \`<scratchpad>\` tags completely, blending the scratchpad thoughts into the main text.
- **Accuracy:** Claude isolated the mathematical gotchas flawlessly (like the `\alpha / r` scaling). ChatGPT tried to be "helpful" by generating literal PyTorch `nn.Module` code, which completely missed the point of the prompt (which was to summarize the *paper's math*, not write the code for me). 
- **Conclusion:** Claude is vastly superior for following strict formatting architectures and step-decomposition instructions.

---

## Final Reusable Template

**Role:** Act as an elite AI researcher mentoring a junior engineer. 

**Context:** Summarize the provided ML research paper. I am asking because I need to implement this specific algorithm in PyTorch today, and I only care about the core mathematics. 

**Example:** For example, do not define basic terms; instead, tell me exactly how the core matrices are initialized and multiplied.

**Step Decomposition:** Before outputting the summary, use a \`<scratchpad>\` block to identify exactly which equations are required for the implementation and mathematically verify their tensor dimensions.

**Output Structure:** Once you have verified the math in the scratchpad, output your summary strictly using the following format:
### 1. The Core Equation
### 2. Tensor Shapes
### 3. Implementation Gotchas

**Paper Text:**
[INSERT RESEARCH PAPER TEXT HERE]

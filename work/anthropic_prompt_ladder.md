# Anthropic Prompt Ladder: Summarizing Advanced ML Research Papers

**Task Source:** FL-01 Workflow Audit (Target Task 3: Summarizing Advanced ML Research Papers for PyTorch Implementation)

---

## The Baseline
**Prompt:** "Summarize this ML research paper. [Paper Text]"

**Output Excerpt:**
*"This groundbreaking paper introduces a novel architecture for language modeling. It achieves state-of-the-art results on several benchmarks by optimizing the attention mechanism..."*

**Notes:**
- **What changed:** (Baseline)
- **What improved:** N/A. 
- **What failed:** It just rewrote the abstract using generic marketing fluff. It gave me zero mathematical insights on how to actually code the algorithm.

---

## Version 1: Role Assignment
**Prompt:** "Act as an elite AI researcher mentoring a junior engineer. Summarize this ML research paper. [Paper Text]"

**Output Excerpt:**
*"Let's break down the architecture. The authors modified the standard transformer block by replacing the dense feed-forward layer with a sparse routing mechanism..."*

**Notes:**
- **What changed:** Added **Role Assignment** ("elite AI researcher mentoring a junior").
- **What improved:** The tone instantly shifted. It stopped using words like "groundbreaking" and adopted a direct, technical vocabulary.
- **What failed:** It was still just a massive wall of text that summarized the entire paper, including the irrelevant "Related Works" section.

---

## Version 2: Context and Motivation
**Prompt:** "Act as an elite AI researcher mentoring a junior engineer. Summarize this ML research paper. I am asking because I need to implement this specific algorithm in PyTorch today, and I only care about the core mathematics. [Paper Text]"

**Output Excerpt:**
*"Skipping the theoretical background, the core algorithm relies on a modified loss function. The primary equation you need to implement is L = \alpha * L_{ce} + \beta * L_{reg}..."*

**Notes:**
- **What changed:** Added **Context and Motivation** (implementing in PyTorch today).
- **What improved:** The AI completely ignored the introductory and background sections of the paper, saving me from reading paragraphs of useless context.
- **What failed:** It gave me the equations, but it explained them like I was a beginner who didn't know what a loss function was, which wasted space.

---

## Version 3: Few-Shot Examples
**Prompt:** "Act as an elite AI researcher mentoring a junior engineer. Summarize this ML research paper. I am asking because I need to implement this specific algorithm in PyTorch today, and I only care about the core mathematics. Example of what I want: If the paper is about LoRA, do not define fine-tuning; instead, tell me exactly how matrices A and B are initialized and multiplied. [Paper Text]"

**Output Excerpt:**
*"The Q and K matrices are initialized using a truncated normal distribution with standard deviation 0.02. The dot product is scaled by the square root of the head dimension (d_k=64) before the softmax..."*

**Notes:**
- **What changed:** Added a **Few-Shot Example** (the LoRA matrix initialization).
- **What improved:** It completely dropped basic ML definitions and instantly provided the exact tensor initializations required for my code.
- **What failed (The "This didn't help" moment):** The output became a chaotic brain-dump of math. It was highly accurate, but impossible to skim. It was technically dense but structurally a mess.

---

## Version 4: Output Structure
**Prompt:** "Act as an elite AI researcher mentoring a junior engineer. Summarize this ML research paper. I am asking because I need to implement this specific algorithm in PyTorch today, and I only care about the core mathematics. Example of what I want: If the paper is about LoRA, do not define fine-tuning; instead, tell me exactly how matrices A and B are initialized. 
Output your summary strictly in this format:
1. The Core Equation
2. Tensor Shapes
3. Implementation Gotchas
[Paper Text]"

**Output Excerpt:**
*"### 1. The Core Equation
...
### 2. Tensor Shapes
- Input: [Batch, Seq_Len, Hidden_Dim]
...
### 3. Implementation Gotchas
- Ensure you apply the scaling factor before the softmax, otherwise gradients will vanish..."*

**Notes:**
- **What changed:** Added **Output Structure**.
- **What improved:** The chaotic math was perfectly organized into three highly scannable headers. I can now look directly at "Tensor Shapes" while writing my code.
- **What failed:** In the "Gotchas" section, the AI occasionally hallucinated minor tensor dimensions because it rushed to format the output instead of reading the paper carefully.

---

## Version 5: Step Decomposition
**Prompt:** "Act as an elite AI researcher mentoring a junior engineer. Summarize this ML research paper. I am asking because I need to implement this specific algorithm in PyTorch today, and I only care about the core mathematics. Example of what I want: If the paper is about LoRA, do not define fine-tuning; instead, tell me exactly how matrices A and B are initialized. 
Before outputting, use a <scratchpad> block to identify exactly which equations are required for implementation and verify their tensor dimensions.
Then, output your summary strictly in this format:
1. The Core Equation
2. Tensor Shapes
3. Implementation Gotchas
[Paper Text]"

**Output Excerpt:**
*"<scratchpad>
Scanning methodology... The paper defines the multi-head mechanism in Eq 4. The tensor shape for the hidden states is [B, L, D]. Wait, Eq 5 specifies a dynamic sequence length, so L is variable. I need to highlight this in the gotchas.
</scratchpad>
### 1. The Core Equation..."*

**Notes:**
- **What changed:** Added **Step Decomposition** (`<scratchpad>`).
- **What improved:** Accuracy skyrocketed. By forcing the AI to think step-by-step and verify the dimensions *before* generating the formatted output, hallucinations dropped to zero.

---

## Cross-Model Comparison (Claude vs. ChatGPT)
I ran the exact final prompt (Version 5) through both Claude 3.5 Sonnet and ChatGPT (GPT-4o).
- **Tone & Structure:** Claude adhered perfectly to the requested structure and kept the tone strictly academic and precise. ChatGPT ignored the XML tags completely, blending the scratchpad thoughts into the main text.
- **Accuracy:** Claude isolated the mathematical gotchas flawlessly. ChatGPT tried to be "helpful" by generating literal Python code, which completely missed the point of the prompt (which was to summarize the *paper's math*, not write the code for me). 
- **Conclusion:** Claude is vastly superior for following strict formatting architectures and step-decomposition instructions.

---

## Final Reusable Template

**Role:** Act as an elite AI researcher mentoring a junior engineer. 
**Context:** Summarize the provided ML research paper. I am asking because I need to implement this specific algorithm in PyTorch today, and I only care about the core mathematics. 
**Example:** If the paper is about LoRA, do not define fine-tuning; instead, tell me exactly how matrices A and B are initialized and multiplied.
**Step Decomposition:** Before outputting the summary, use a `<scratchpad>` block to identify exactly which equations are required for the implementation and mathematically verify their tensor dimensions.
**Output Structure:** Once you have verified the math in the scratchpad, output your summary strictly using the following format:
### 1. The Core Equation
### 2. Tensor Shapes
### 3. Implementation Gotchas

**Paper Text:**
[INSERT RESEARCH PAPER TEXT HERE]

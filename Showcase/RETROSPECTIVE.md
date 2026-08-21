# FlyRank ML Internship: Final Retrospective

*Written for the person I was in Week 1.*

## What I Set Out to Do vs. What Changed
When I started this internship in Week 1, my primary mindset was simply, "What am I going to learn this time?" I had done projects before, but I was incredibly glad to finally get my hands on something real. Working alongside a company like FlyRank—a team that clearly cares about real, substantive AI work just as much as I do—was exactly the environment I was looking for. My highest expectation was to impress the company enough that they would consider hiring me full-time. I wanted to prove that I wasn't just someone who could string API calls together, but an engineer who could think rigorously about data, leakage, and architecture.

What changed wasn't my desire to be hired, but my understanding of what "real AI work" actually looks like. At the start, it's easy to assume that the hardest part of Machine Learning is writing the model architecture or tuning hyperparameters. In reality, I spent the majority of my time wrestling with the unglamorous truths of applied ML: hunting down data leakage, validating signals honestly, and recognizing when a model is mathematically bound by proxy labels. 

## What I Would Build Next
As proud as I am of the V1 pipeline, the evaluation process revealed a glaring limitation: the cold-start problem. The V1 model is functionally blind to brand new, zero-history content. 

My next step is the **V2 Zero-Shot Architecture Proposal**—a Model Cascade utilizing a structural web crawler and a fine-tuned LoRA model. However, building V2 isn't just a matter of having a few more weeks to code. The real bottleneck is scalability. A true V2 requires significant resources: API costs, crawler infrastructure, testing platforms, and deep domain knowledge across frontend and backend engineering. My hands are tied to theory-building on paper for now. To actually build this at scale, I need FlyRank's infrastructure and team. If my proposal proves its worth, I would love the opportunity to come on board full-time and build it into a reality together.

## The Three Most Transferable Things I Learned

**1. Independent Workflow**
I didn't come from a highly structured background; my ML journey started by being thrown into the dark forest, piecing together fragments of truth on my own. Through this internship, I learned what an independent workflow actually means in a professional setting. I experienced firsthand the real limits—and the distinct benefits—of tackling an end-to-end system completely solo versus working within a larger engineering team. 

**2. Professionality in ML**
When I was first learning ML, my only goal was to "make it work," regardless of how messy the code or the logic got. Here, I learned that making it work is only the baseline. True professionality means keeping the system updated, documenting work rigorously, and developing a strict ethical standard to always review your own outputs. More importantly, I learned how to make my work *marketable*. I was tasked with building a core model, but I realized that a model alone isn't a product. By building a complete backend architecture, an interface, and a LLaMA chatbot to translate the math into strategy, I learned how to package raw ML into a flashy, tangible product that FlyRank could actually sell. That product-minded engineering is something courses simply don't teach.

**3. Real Experience Working on Real, Messy Data**
The 30,000-row dataset was a masterclass in the realities of production data. Dealing with `NaN` values, understanding proxy labels, and structuring a `GroupShuffleSplit` were invaluable lessons. You can't learn how to handle data leakage from clean Kaggle datasets; you have to get into the weeds of real-world data.

## A Final Note of Appreciation
Having studied entirely on my own for so long without any formal, structured coursework, this internship brought me a profound sense of genuine happiness. For the first time, I had real mentors watching over my work—offering real criticism and real appreciation. FlyRank gave me a chance to learn what it means to be a professional ML engineer. I am deeply grateful for this opportunity, and I genuinely hope I can join the team full-time to contribute to the company's goals moving forward.

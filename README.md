Artificial Intelligence Projects – Fall 2024  
 

This repository contains three major Artificial Intelligence projects completed as part of 'CIS 561 – Artificial Intelligence (Fall 2024)'.  
Each project explores a different AI problem category, including optimization, multimodal learning, and autonomous agents.

---

'Project 1: Traveling Salesman Problem (TSP)'  
 

This project studies the 'Traveling Salesman Problem (TSP)' — an NP-hard optimization problem where the goal is finding the shortest route visiting all cities exactly once.

Topics Covered
- What is TSP?  
- Real-world applications (logistics, manufacturing, robotics, telecommunications, chemistry)  
- Approximate & heuristic algorithms:
  - Greedy  
  - Genetic Algorithm  
  - Simulated Annealing  
  - Ant Colony Optimization  
  - Tabu Search  
  - Particle Swarm Optimization  
  - Nearest Neighbor  
  - k-Opt & Lin-Kernighan  
  - Dynamic Programming (Held-Karp)  
  - Iterated Local Search  
  - Bee Colony Optimization  
  - Memetic Algorithms  
  - Neural Networks  

Task 2 – Genetic Algorithm Implementation
Using a GA to solve TSP for '10 cities', starting and ending at city A.  
The code computes:
- Minimum path length  
- Best visiting order  
- Fitness-based selection, crossover, mutation  

---

Project 2: Multimodal AI – OpenAI CLIP

This project analyzes 'CLIP (Contrastive Language–Image Pre-Training)', a multimodal AI model trained on large-scale image–text pairs.

Topics Covered
- Pre-training with natural language supervision  
- Contrastive learning  
- Large-scale multimodal dataset creation  
- CLIP architecture (Image & Text Transformers)  
- Zero-shot prediction  
- Distribution shift robustness  
- Comparison to human reasoning  
- Model limitations & future directions  

Highlights
- CLIP performs classification using 'text prompts instead of labels' 
- Strong generalization across unseen datasets  
- Sensitive to prompt wording  
- Inherits data biases  
- Future improvements include prompt engineering, scene graphs, multimodal extensions (audio/video)

---

Project 3: Autonomous Agent – Auto-GPT Email Manager  


This project configures an 'Auto-GPT agent' enhanced with an 'Email Plugin' to autonomously send, read, and reply to emails.

Task 1: Installation
- Clone Auto-GPT  
- Create and activate virtual environment  
- Install dependencies  
- Add OpenAI API key to `.env`  

Task 2: Plugin Setup
- Clone Auto-GPT Plugins repo  
- Install Email Plugin  
- Configure SMTP & IMAP  
- Validate plugin detection  
- Test automated email sending  

Email Automation
Example email used in the project:
```python
yag.send(
    to='vmeghana890@gmail.com',
    subject='Invitation to my Birthday Party',
    contents='Hello, I’m Meghana. The party starts at 8 pm this Friday...'
)

# 🕹️ Retro PokeCounter

Hi! 👋 This is my first web project using Python Flask. It's a web that helps you find the best types to use against a specific Pokemon in a battle.

## 💡 Why I Built This
I actually built this because I play a lot of **Pokemon GO**. 
Whenever I tried to fight a **Raid Boss**, I never knew which Pokemon to use to win. I kept guessing and losing! Thus, I wanted a tool that would tell me exactly what types are strong against the boss so I could make a wiser choice and pick the perfect team.

So, I decided to build my own "Smart Pokedex" to solve that problem.

## 📝 What does it do?

You can type in a Pokemon's name (like "Charizard" or "Mewtwo"), and the app tells you:
1.  **What type it is.**
2.  **Its biggest weaknesses** (calculated using my own math).
3.  **A cool picture** of the Pokemon so you know who you are fighting.

I built this project to practice **Python**, learn how to use **APIs**, and get better at **CSS layouts**.

## ✨ Cool Features

* **Retro Design:** I used a pixel font called "Press Start 2P" and some CSS tricks to make the red case, the blinking lights, and the screen look like a retro device.
* **Custom Math:** Instead of the standard game rules, I wrote my own code to calculate damage multipliers.
* **Real Data:** It connects to the [PokeAPI](https://pokeapi.co/), so it works for almost every Pokemon.
* **Type Icons:** It shows the actual symbols for Fire, Water, etc., instead of just text.

## 🛠️ Tools I Used

* **Python & Flask:** For the backend code.
* **HTML & CSS:** For the design and layout (I used Flexbox!).
* **Jinja2:** To show the Python data on the HTML page.
* **PokeAPI:** To get all the Pokemon data.

## 🧮 How the Math Works

I wanted to try something different, so I used my own numbers to figure out weaknesses:

* **Super Effective:** x1.6 damage
* **Not Very Effective:** x0.625 damage
* **Immune:** x0.39 damage

If a Pokemon has two types (like Charizard is Fire/Flying), my code multiplies these numbers. So if Rock is super effective against *both* Fire and Flying, the damage becomes **x2.56**!

## 💻 How to Run It

If you want to try this on your computer, here is the web: pokecounter.vercel.app

---
*Built by Dave Danh*

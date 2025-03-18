# Fruit Information AI Model 🍎🍌🍇

This is a **simple yet advanced AI model** built using Python that can respond to questions about various fruits in a natural, human-like manner. It also greets users when they say "Hello" or similar phrases. The model uses **Count Vectorization** and **Naive Bayes Classification** for text understanding and response generation.

## 📌 Features
- Provides information about a wide range of fruits.
- Human-like conversational responses.
- Efficient text understanding using Count Vectorization.
- Trained on various prompts to ensure robust communication.
- Easily expandable with more fruits and conversational prompts.

## 📚 Requirements
Install the required libraries via pip:
```bash
pip install scikit-learn
```

## 🔍 How It Works
1. The model is trained on a dataset of fruit-related questions and greetings.
2. Uses **Count Vectorization** for vectorizing input text.
3. **Naive Bayes Classifier** is used for text classification and prediction.
4. Responses are stored and retrieved based on predictions.

## 🚀 Usage
```bash
python your_model_file.py
```
The model will now await your input. Type something like:
- "What is a Banana?"
- "Tell me about Mango."
- "Hey!"
- "What's special about Grapes?"
- "What nutrients do Apples have?"

## 🤖 Example Conversation
```plaintext
You: Hi
Fruity AI: Hello! How can I assist you today? Feel free to ask me about any fruit you want to know about!

You: What is a Pineapple?
Fruity AI: Pineapples are tropical fruits with juicy, sweet, and tangy yellow flesh. Rich in vitamins and enzymes.
```

## 📺 Embeds Preview
You can also add **beautiful embeds** to enhance user experience by modifying the bot's responses to include rich text formatting.

Example Embed Response:
```python
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Bot is ready as {bot.user}')

@bot.command()
async def fruit(ctx, *, query):
    embed = discord.Embed(title="Fruity AI Response", description=f"Here's what I found about {query}:", color=0x00ff00)
    embed.add_field(name="Information", value="Pineapples are tropical fruits with juicy, sweet, and tangy yellow flesh. Rich in vitamins and enzymes.", inline=False)
    embed.set_footer(text="Fruity AI - Your Fruit Expert")
    await ctx.send(embed=embed)

bot.run('YOUR_BOT_TOKEN')
```

## 📁 Model Training & Saving
The model is trained directly when you run the code. You can expand the model by adding more fruits and conversation prompts.

## 💡 Customization
To add more fruits or improve the model's conversation style, simply:
- Expand the `training_texts` and `training_labels` lists.
- Update the `info` dictionary with more information.

## 🌟 Future Improvements
- Making the AI sound more human-like with diverse, conversational responses.
- Including fun facts about each fruit.
- Adding continuous learning from user interactions.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Happy coding! 😊


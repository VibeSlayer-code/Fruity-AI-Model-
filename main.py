from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


training_texts = [
    "Tell me about apple", "What is apple?", "Give me information about apple", "Describe an apple", "What are apples?", "What's an apple?", "Can you tell me about apples?", "Explain apple.",
    "Tell me about banana", "What is banana?", "Give me information about banana", "Describe a banana", "What are bananas?", "What's a banana?", "Can you tell me about bananas?", "Explain banana.",
    "Tell me about orange", "What is orange?", "Give me information about orange", "Describe an orange", "What are oranges?", "What's an orange?", "Can you tell me about oranges?", "Explain orange.",
    "Tell me about mango", "What is mango?", "Give me information about mango", "Describe a mango", "What are mangoes?", "What's a mango?", "Can you tell me about mangoes?", "Explain mango.",
    "Tell me about strawberry", "What is strawberry?", "Give me information about strawberry", "Describe a strawberry", "What are strawberries?", "What's a strawberry?", "Can you tell me about strawberries?", "Explain strawberry.",
    "Tell me about grapes", "What are grapes?", "Give me information about grapes", "Describe grapes", "What are grapes?", "What's a grape?", "Can you tell me about grapes?", "Explain grapes.",
    "Tell me about pineapple", "What is pineapple?", "Give me information about pineapple", "Describe a pineapple", "What are pineapples?", "What's a pineapple?", "Can you tell me about pineapples?", "Explain pineapple.",
    "Tell me about watermelon", "What is watermelon?", "Give me information about watermelon", "Describe a watermelon", "What are watermelons?", "What's a watermelon?", "Can you tell me about watermelons?", "Explain watermelon.",
    "Tell me about kiwi", "What is kiwi?", "Give me information about kiwi", "Describe a kiwi", "What are kiwis?", "What's a kiwi?", "Can you tell me about kiwis?", "Explain kiwi.",
    "Tell me about blueberry", "What is blueberry?", "Give me information about blueberry", "Describe a blueberry", "What are blueberries?", "What's a blueberry?", "Can you tell me about blueberries?", "Explain blueberry.",
    "Hello", "Hi", "Hey", "Good morning", "Good evening", "Greetings", "What's up?"
]

training_labels = [
    "Apple", "Apple", "Apple", "Apple", "Apple", "Apple", "Apple", "Apple",
    "Banana", "Banana", "Banana", "Banana", "Banana", "Banana", "Banana", "Banana",
    "Orange", "Orange", "Orange", "Orange", "Orange", "Orange", "Orange", "Orange",
    "Mango", "Mango", "Mango", "Mango", "Mango", "Mango", "Mango", "Mango",
    "Strawberry", "Strawberry", "Strawberry", "Strawberry", "Strawberry", "Strawberry", "Strawberry", "Strawberry",
    "Grapes", "Grapes", "Grapes", "Grapes", "Grapes", "Grapes", "Grapes", "Grapes",
    "Pineapple", "Pineapple", "Pineapple", "Pineapple", "Pineapple", "Pineapple", "Pineapple", "Pineapple",
    "Watermelon", "Watermelon", "Watermelon", "Watermelon", "Watermelon", "Watermelon", "Watermelon", "Watermelon",
    "Kiwi", "Kiwi", "Kiwi", "Kiwi", "Kiwi", "Kiwi", "Kiwi", "Kiwi",
    "Blueberry", "Blueberry", "Blueberry", "Blueberry", "Blueberry", "Blueberry", "Blueberry", "Blueberry",
    "Greeting", "Greeting", "Greeting", "Greeting", "Greeting", "Greeting", "Greeting"
]

info = {
    "Apple": "Apples are sweet, edible fruits produced by apple trees. They are rich in fiber, vitamin C, and antioxidants.",
    "Banana": "Bananas are long, yellow fruits high in potassium and provide quick energy. Grown in tropical regions.",
    "Orange": "Oranges are citrus fruits known for their high vitamin C content and refreshing taste.",
    "Mango": "Mangoes are tropical fruits with juicy, sweet flesh. They are rich in vitamins A and C.",
    "Strawberry": "Strawberries are bright red fruits with a sweet taste, rich in vitamin C and antioxidants.",
    "Grapes": "Grapes are small, round fruits that grow in clusters. They can be eaten fresh or used to make wine.",
    "Pineapple": "Pineapples are tropical fruits with juicy, sweet, and tangy yellow flesh. Rich in vitamins and enzymes.",
    "Watermelon": "Watermelons are large fruits with sweet, juicy, red flesh. Great for hydration and packed with vitamins.",
    "Kiwi": "Kiwis are small fruits with green flesh and tiny black seeds. They are rich in vitamin C and fiber.",
    "Blueberry": "Blueberries are small, round, blue fruits known for their antioxidant properties and sweet-tart taste.",
    "Greeting": "Hello! How can I assist you today?"
}


vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_texts)

model = MultinomialNB()
model.fit(X_train, training_labels)



def get_response(user_input: str) -> str:
    X_test = vectorizer.transform([user_input])
    prediction = model.predict(X_test)[0]
    return info.get(prediction, "I'm sorry, I don't understand that.")



while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    response = get_response(user_input)
    print(f"Fruity AI: {response}")

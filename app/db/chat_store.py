from app.db.mongo_client import chat_collection

def save_chat(user_id, query, response):
    chat_collection.insert_one({
        "user_id": user_id,
        "query": query,
        "response": response
    })

def get_chat_history(user_id):
    chats = chat_collection.find({"user_id": user_id})

    history = ""
    for chat in chats:
        history += f"\nUser: {chat['query']}\nAssistant: {chat['response']}"

    return history
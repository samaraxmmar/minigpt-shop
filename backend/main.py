from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
import json
import asyncio
from datetime import datetime

# Load environment variables
load_dotenv()

app = FastAPI(title="MiniGPT-Shop API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class ChatMessage(BaseModel):
    message: str
    user_id: Optional[str] = "anonymous"

class ChatResponse(BaseModel):
    response: str
    products: Optional[List[dict]] = None
    timestamp: str

class Product(BaseModel):
    id: str
    name: str
    price: float
    description: str
    image_url: str
    rating: float
    features: List[str]
    category: str

# Mock product database
MOCK_PRODUCTS = [
    {
        "id": "phone_001",
        "name": "Samsung Galaxy A54 5G",
        "price": 349.99,
        "description": "Smartphone with excellent camera and 5G connectivity",
        "image_url": "https://via.placeholder.com/300x300/007bff/ffffff?text=Samsung+A54",
        "rating": 4.3,
        "features": ["50MP main camera", "32MP front camera", "6.4 inch Super AMOLED", "5000mAh battery", "5G ready"],
        "category": "smartphone"
    },
    {
        "id": "phone_002", 
        "name": "Google Pixel 7a",
        "price": 399.99,
        "description": "Google's AI-powered smartphone with exceptional photography",
        "image_url": "https://via.placeholder.com/300x300/34a853/ffffff?text=Pixel+7a",
        "rating": 4.5,
        "features": ["64MP main camera", "13MP ultrawide", "6.1 inch OLED", "4385mAh battery", "Google AI features"],
        "category": "smartphone"
    },
    {
        "id": "phone_003",
        "name": "iPhone 14",
        "price": 799.99,
        "description": "Apple's flagship smartphone with advanced camera system",
        "image_url": "https://via.placeholder.com/300x300/000000/ffffff?text=iPhone+14",
        "rating": 4.6,
        "features": ["48MP main camera", "12MP ultrawide", "6.1 inch Super Retina XDR", "3279mAh battery", "A16 Bionic chip"],
        "category": "smartphone"
    },
    {
        "id": "laptop_001",
        "name": "MacBook Air M2",
        "price": 1199.99,
        "description": "Powerful and efficient laptop with Apple Silicon",
        "image_url": "https://via.placeholder.com/300x300/c0c0c0/000000?text=MacBook+Air",
        "rating": 4.7,
        "features": ["M2 chip", "13.6 inch Liquid Retina", "18-hour battery", "8GB RAM", "256GB SSD"],
        "category": "laptop"
    },
    {
        "id": "headphones_001",
        "name": "Sony WH-1000XM5",
        "price": 349.99,
        "description": "Premium noise-canceling wireless headphones",
        "image_url": "https://via.placeholder.com/300x300/000000/ffffff?text=Sony+WH1000XM5",
        "rating": 4.4,
        "features": ["30-hour battery", "Industry-leading noise canceling", "Multipoint connection", "Quick charge", "Premium sound"],
        "category": "headphones"
    }
]

# Simple AI response logic (mock)
def generate_ai_response(user_message: str) -> dict:
    message_lower = user_message.lower()
    
    # Extract budget if mentioned
    budget = None
    if "€" in message_lower or "euro" in message_lower:
        words = message_lower.split()
        for i, word in enumerate(words):
            if "€" in word or word == "euro":
                try:
                    if i > 0:
                        budget = float(words[i-1].replace("€", "").replace(",", "."))
                    elif i < len(words) - 1:
                        budget = float(words[i+1].replace("€", "").replace(",", "."))
                except:
                    pass
    
    # Determine product category
    category = None
    if any(word in message_lower for word in ["phone", "smartphone", "téléphone", "mobile"]):
        category = "smartphone"
    elif any(word in message_lower for word in ["laptop", "ordinateur", "pc", "macbook"]):
        category = "laptop"
    elif any(word in message_lower for word in ["headphones", "casque", "écouteurs"]):
        category = "headphones"
    
    # Filter products
    filtered_products = MOCK_PRODUCTS.copy()
    
    if category:
        filtered_products = [p for p in filtered_products if p["category"] == category]
    
    if budget:
        filtered_products = [p for p in filtered_products if p["price"] <= budget]
    
    # Sort by rating
    filtered_products.sort(key=lambda x: x["rating"], reverse=True)
    
    # Limit to top 3
    filtered_products = filtered_products[:3]
    
    # Generate response text
    if not filtered_products:
        response_text = "I'm sorry, I couldn't find any products matching your criteria. Could you please provide more details about what you're looking for?"
    else:
        if category == "smartphone":
            response_text = f"Great! I found {len(filtered_products)} excellent smartphones"
            if budget:
                response_text += f" under €{budget}"
            response_text += " with great cameras. Here are my top recommendations:"
        else:
            response_text = f"I found {len(filtered_products)} great products for you. Here are my recommendations:"
    
    return {
        "response": response_text,
        "products": filtered_products
    }

@app.get("/")
async def root():
    return {"message": "MiniGPT-Shop API is running!"}

@app.post("/chat", response_model=ChatResponse)
async def chat_with_ai(message: ChatMessage):
    try:
        # Generate AI response
        ai_result = generate_ai_response(message.message)
        
        response = ChatResponse(
            response=ai_result["response"],
            products=ai_result["products"],
            timestamp=datetime.now().isoformat()
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/products")
async def get_all_products():
    return {"products": MOCK_PRODUCTS}

@app.get("/products/{product_id}")
async def get_product(product_id: str):
    product = next((p for p in MOCK_PRODUCTS if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


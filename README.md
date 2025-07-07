# MiniGPT-Shop – Smart AI Shopping Assistant

An intelligent chatbot that helps you choose products online based on your needs and budget. MiniGPT-Shop offers a seamless and personalized AI-assisted shopping experience, like a smart tech seller always available.

![Main Interface](screenshots/01-interface-initiale.webp)

## 🧠 Key Features

### Natural Interaction
Users can chat naturally with the chatbot, in either French or English. The AI understands language nuances and can interpret complex requests including specific criteria like budget, intended use, and personal preferences.

### Intelligent Need Understanding
The AI automatically analyzes user messages to extract:
- **Budget**: Automatic detection of mentioned amounts (€ or euros)
- **Product Category**: Smartphones, laptops, headphones, etc.
- **Specific Criteria**: Camera quality, battery life, special features
- **Usage Preferences**: Professional, personal, gaming, music, etc.

### Relevant Product Suggestions
The system suggests suitable products based on a mocked but realistic database, including:
- **Filtered products** according to user criteria
- **Detailed information**: Price, ratings, main features
- **Visual comparison** with interactive product cards
- **Smart sorting** by relevance and user ratings

![Smartphone Response Example](screenshots/02-reponse-smartphone.webp)

### Modern User Interface
- **Responsive design** for mobile and desktop
- **Intuitive chat interface** with conversation bubbles
- **Elegant product cards** with images, prices, and features
- **Smooth animations** and loading indicators
- **Modern theme** with gradients and subtle shadows

![Headphones Response Example](screenshots/03-reponse-ecouteurs.webp)

## 💻 Technologies Used

### Frontend – React with Next.js
- **React 18** with modern hooks (useState, useEffect, useRef)
- **Vite** as a bundler for optimal performance
- **Tailwind CSS** for fast and consistent styling
- **shadcn/ui** for professional UI components
- **Lucide React** for modern and consistent icons
- **Responsive design** with full mobile support

### Backend – FastAPI
- **FastAPI** for a modern and performant REST API
- **Pydantic** for data validation
- **CORS** configured for cross-origin requests
- **Uvicorn** as a high-performance ASGI server
- **Modular architecture** with clear separation of concerns

### Artificial Intelligence (Extensible)
- **Natural language processing logic** built-in
- **Smart product filtering system**
- **Architecture ready** for integration with OpenAI or Mistral
- **Support planned** for Pinecone (vector search)
- **Extensible AI pipeline** using LangChain

### Database and Search
- **Mocked database** with realistic products
- **Filtering system** by category, price, and features
- **Architecture prepared** for Pinecone (RAG)
- **Semantic search** (future implementation)

## 📦 Project Structure

```
minigpt-shop/
├── backend/                 # API FastAPI
│   ├── main.py             # Point d'entrée de l'API
│   ├── requirements.txt    # Dépendances Python
│   └── .env               # Variables d'environnement
├── frontend/               # Application React
│   ├── src/
│   │   ├── App.jsx        # Composant principal
│   │   ├── App.css        # Styles Tailwind
│   │   └── components/    # Composants UI
│   ├── package.json       # Dépendances Node.js
│   └── index.html         # Point d'entrée HTML
├── screenshots/           # Captures d'écran pour documentation
└── README.md             # Documentation principale
```


## 🚀 Installation and Launch

### Prerequisites
- **Python 3.11+** installed
- **Node.js 18+** and **pnpm** for frontend
- **Git** to clone the repository

### 1. Clone the repository
```bash
git clone https://github.com/your-username/minigpt-shop.git
cd minigpt-shop

```

### 2. Backend Setup
```bash
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Configure environment variables (optional)
cp .env.example .env
# Edit .env with your API keys if needed

# Start the backend server
python main.py

```

Backend will be available at `http://localhost:8000`

### 3. Frontend Setup
```bash
cd frontend

# Install Node.js dependencies
pnpm install

# Start development server
pnpm run dev --host

```

Frontend will be available at`http://localhost:5173`

### 4. Access the App
Open your browser and go to `http://localhost:5173`to start using MiniGPT-Shop..


*MiniGPT-Shop represents the future of online shopping with a personalized and intelligent AI assistant. The modular and extensible architecture allows for continuous evolution toward even more advanced features.*


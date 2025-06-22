# AI Test Generator 🚀

This is a reusable GenAI-powered agentic tool that scans a React frontend and auto-generates functional UI test classes using Selenium, TestNG, and the Page Object Model (POM).

---

## 🧩 What It Does
- Clones your frontend GitHub repo
- Extracts JSX/TSX components
- Sends them to OpenAI for intelligent test generation
- Writes Page Object + TestNG classes
- Copies generated files into a Maven-compatible test suite

---

## 🛠 Prerequisites
- Python 3.8+
- Java + Maven
- Google Chrome + chromedriver in PATH
- OpenAI API key

---

## ⚙️ Setup

```bash
git clone <this-repo>
cd ai-test-generator-reusable

# Set up environment
cp .env.example .env
# Add your OpenAI key to .env

# Install dependencies
pip install -r requirements.txt
```

---

## 🔧 Configuration

Edit `config/settings.json` if you don’t want to pass arguments every time:

```json
{
  "repo_url": "https://github.com/your-org/your-react-repo",
  "frontend_path": "frontend/src"
}
```

---

## 🚀 Run It

### Option 1: Use config file
```bash
python run_pipeline.py
```

### Option 2: Pass arguments via CLI
```bash
python run_pipeline.py --repo=https://github.com/your-org/your-repo --path=frontend/src/components
```

---

## 🧪 Test Execution

Navigate to the generated Maven project:

```bash
cd functional-tests
mvn test
```

---

## 📦 Output

Generated test classes are saved into:

- `functional-tests/src/test/java/pages/`
- `functional-tests/src/test/java/tests/`

---

## 🧠 How It Works
Each run:
- Skips unchanged components using file hashing
- Refactors old tests using OpenAI if the JSX is updated
- Maintains registries for test coverage and source versions

---

## 🤝 Contributions
- Edit the LLM prompt at `prompts/testng_pom_prompt.txt`
- Customize Maven test template in `functional-tests/`
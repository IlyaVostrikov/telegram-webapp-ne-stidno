git config --global user.name "Ilya Vostrikov"
git config --global user.email "ilyavostrikov90@gmail.com"   # ← свой GitHub email
git remote remove origin
git remote add origin https://github.com/IlyaVostrikov/telegram-webapp-ne-stidno.git
git branch -M main
git push -u origin main

# Создаём index.html
echo "<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>Telegram WebApp</title>
  <link rel=\"stylesheet\" href=\"style.css\">
  <script src=\"script.js\" defer></script>
</head>
<body>
  <h1>Добро пожаловать в Telegram WebApp</h1>
  <button id=\"send\">Нажми меня</button>
</body>
</html>" > index.html

# Создаём style.css
echo "/* style.css */
body {
  margin: 0;
  font-family: sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f2f2f2;
}

button {
  background-color: #0088cc;
  color: white;
  border: none;
  padding: 12px 24px;
  font-size: 16px;
  border-radius: 8px;
  cursor: pointer;
}

button:hover {
  background-color: #006699;
}" > style.css

# Создаём Vercel конфигурацию
echo "{
  \"version\": 2,
  \"builds\": [
    { \"src\": \"index.html\", \"use\": \"@vercel/static\" }
  ],
  \"routes\": [
    { \"src\": \"/(.*)\", \"dest\": \"index.html\" }
  ]
}" > vercel.json

git add .
git commit -m "Добавлены style.css, index.html и vercel.json для деплоя на Vercel"
git push

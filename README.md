# 📝 Simple Static Blog Server

A lightweight Python server to host a static blog with dynamic post data — built using only the Python standard library.

## 🚀 Description

This project serves:

- `index.html` as the homepage (`/`)
- Static assets (CSS, JS)
- A `/posts` API endpoint that delivers blog post data from a local `posts.json` file

It’s designed for minimal setup and can be deployed easily on platforms like [Render](https://render.com).

## 🌟 Features

- ✅ Serves `index.html` at `/`
- 🎨 Serves static CSS and JS files
- 📰 REST endpoint at `/posts` (reads from `posts.json`)
- 🐍 Uses only Python’s built-in `http.server`
- ☁️ Fully compatible with Render.com

## 📂 Folder Structure

```
.
├── blog_server.py       # Python server
├── index.html           # Main HTML file
├── style.css            # Blog styling
├── script.js            # Frontend logic (fetching posts)
└── posts.json           # Blog post data
```

## 🧪 Local Development

1. Clone or download the repo, and make sure all files are in the same directory.
2. Run the server:
   ```bash
   python blog_server.py
   ```
3. Open your browser and navigate to:  
   `http://127.0.0.1:7000`

## 🛠️ Deploying to Render

1. Push your code to a public GitHub repo.
2. Create a new **Web Service** on [Render](https://dashboard.render.com/).
3. Use the following settings:
   - **Environment:** Python 3
   - **Start Command:** `python blog_server.py`
   - **Port:** Automatically detected (set with `PORT = int(os.environ.get("PORT", 7000))` in your code)
4. Deploy!

📘 Docs: [Render Web Services Port Binding](https://render.com/docs/web-services#port-binding)

## 📡 Sample `/posts` API Response

```json
[
  {
    "title": "Hello World",
    "content": "This is my first blog post.",
    "author": "Belam Muia",
    "date": "2025-07-19"
  },
  {
    "title": "Another Day",
    "content": "Learning to build with Python!",
    "author": "Belam Muia",
    "date": "2025-07-20"
  }
]
```

## 🚧 Future Improvements

- Add support for POST/PUT to add/edit blog posts
- Add markdown rendering support
- Add basic routing with JavaScript
- Improve error handling
- Add tests for API responses

## 📬 Contact

**Belam Muia**  
📧 [belammuia0@gmail.com](mailto:belammuia0@gmail.com)

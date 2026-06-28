import os

products = [
    {
        "filename": "product-indian-army.html",
        "name": "Indian Army Soft Cotton T-Shirt",
        "price": "<span class=\"old-price\">?599.00</span>?499.00",
        "image": "ChatGPT Image Jun 28, 2026, 02_55_22 PM.png"
    },
    {
        "filename": "product-indian-air-force.html",
        "name": "Indian Air Force Soft Cotton T-Shirt",
        "price": "<span class=\"old-price\">?599.00</span>?449.00",
        "image": "ChatGPT Image Jun 28, 2026, 02_55_15 PM.png"
    },
    {
        "filename": "product-flying-rafael.html",
        "name": "?Flying Rafael Soft Cotton T-Shirt",
        "price": "?390.00",
        "image": "ChatGPT Image Jun 28, 2026, 02_55_26 PM.png"
    },
    {
        "filename": "product-nautical-miles.html",
        "name": "?Nautical Miles Soft Cotton T-Shirt",
        "price": "?490.00",
        "image": "ChatGPT Image Jun 28, 2026, 02_55_30 PM.png"
    },
    {
        "filename": "product-land-warfare.html",
        "name": "Land Warfare Soft Cotton T-Shirt",
        "price": "?520.00",
        "image": "90827efd-ab67-4926-b6e6-ee890d25b840.jpg"
    },
    {
        "filename": "product-indian-navy.html",
        "name": "Indian Navy Soft Cotton T-Shirt",
        "price": "?599.00",
        "image": "3e420b37-ccea-4527-bdc0-c1cc787f4041.jpg"
    }
]

template = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - CORVIN</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@300;400;500;600;700&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <!-- Announcement Bar -->
    <div class="announcement-bar">
        <marquee behavior="scroll" direction="left">FREE WORLDWIDE SHIPPING ON ALL ORDERS OVER  // NEW MILITARY
            SURPLUS COLLECTION OUT NOW</marquee>
    </div>

    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-links">
            <a href="corvin.html">SHOP</a>
            <a href="corvin.html#latest-drops">COLLECTIONS</a>
        </div>
        <div class="logo">
            <a href="corvin.html"><img src="logo.png" alt="CORVIN"></a>
        </div>
        <div class="nav-links">
            <a href="about.html">ABOUT</a>
            <a href="cart.html">CART (0)</a>
        </div>
    </nav>

    <main class="product-detail-main">
        <div class="product-breadcrumbs">
            <a href="corvin.html">Home</a> / <a href="regular.html">Regular Size Tshirts</a> / <span>{name}</span>
        </div>

        <div class="product-detail-container">
            <!-- Left Side: Images -->
            <div class="product-gallery">
                <img src="{image}" alt="{name}" class="main-image">
                <div class="thumbnail-gallery">
                    <img src="{image}" alt="Thumbnail" class="thumbnail-image active">
                    <!-- Additional thumbnails can be added here -->
                </div>
            </div>

            <!-- Right Side: Details -->
            <div class="product-info-panel">
                <h2 class="product-category-title">Regular Size Tshirts</h2>
                <h1 class="product-title-large">{name}</h1>
                <div class="product-price-large">{price}</div>

                <div class="product-options-group">
                    <div class="options-header">
                        <span class="options-label">Size</span>
                        <button class="btn-clear">Clear</button>
                    </div>
                    <div class="option-buttons">
                        <button class="option-btn">M</button>
                        <button class="option-btn">L</button>
                        <button class="option-btn">XL</button>
                        <button class="option-btn">XXL</button>
                    </div>
                </div>

                <div class="product-options-group">
                    <div class="options-header">
                        <span class="options-label">Color</span>
                    </div>
                    <div class="option-buttons">
                        <button class="option-btn selected">Black</button>
                        <button class="option-btn">White</button>
                        <button class="option-btn">Royal Blue</button>
                    </div>
                </div>

                <div class="cart-actions">
                    <div class="quantity-selector">
                        <button class="quantity-btn">-</button>
                        <input type="text" class="quantity-input" value="1">
                        <button class="quantity-btn">+</button>
                    </div>
                    <button class="btn-add-cart">Add to Cart</button>
                </div>

                <div class="size-chart-section">
                    <h3>Size Chart</h3>
                    <img src="sizechart.png" alt="Size Chart" class="size-chart-img">
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="site-footer">
        <div class="footer-top">
            <h2 class="footer-marquee-text">Corvin <span id="typewriter"></span><span class="typewriter-cursor">|</span></h2>
        </div>
        <div class="footer-middle">
            <p class="sale-text">SALE UP TO 40% OFF FOR ALL CLOTHES.</p>
        </div>
        <div class="footer-bottom">
            <div class="footer-logo-col">
                <img src="logo.png" alt="CORVIN" class="footer-logo">
                <p class="tagline">Precise. Powerful. Corvin.</p>
            </div>
            <div class="footer-links-col">
                <a href="about.html">About us</a>
                <a href="#">Account</a>
                <a href="#">Contact Us</a>
                <a href="returns-policy.html">Refund and Returns Policy</a>
            </div>
            <div class="footer-subscribe-col">
                <p class="subscribe-label">Subscribe</p>
                <form class="subscribe-form">
                    <input type="email" placeholder="Your Email Address... *" required>
                    <button type="submit" class="btn-blue">SUBSCRIBE</button>
                </form>
            </div>
        </div>
        <div class="footer-copyright">
            <p>Copyright &copy; 2026 corvin.in. Powered by corvin.in.</p>
        </div>
    </footer>
    <script>
        const typewriterText = document.getElementById("typewriter");
        const words = ["Powerful.", "Precise."];
        let wordIndex = 0;
        let charIndex = 0;
        let isDeleting = false;

        function type() {
            if(!typewriterText) return;
            const currentWord = words[wordIndex];
            
            if (isDeleting) {
                typewriterText.textContent = currentWord.substring(0, charIndex - 1);
                charIndex--;
            } else {
                typewriterText.textContent = currentWord.substring(0, charIndex + 1);
                charIndex++;
            }

            let typeSpeed = isDeleting ? 40 : 80;

            if (!isDeleting && charIndex === currentWord.length) {
                typeSpeed = 1500; // Pause at end of word
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                wordIndex = (wordIndex + 1) % words.length;
                typeSpeed = 300; // Pause before typing new word
            }

            setTimeout(type, typeSpeed);
        }

        // Start typing animation on load
        document.addEventListener("DOMContentLoaded", () => {
            setTimeout(type, 1000);

            // Option selection logic
            document.querySelectorAll(".option-buttons").forEach(group => {
                const buttons = group.querySelectorAll(".option-btn");
                buttons.forEach(btn => {
                    btn.addEventListener("click", () => {
                        buttons.forEach(b => b.classList.remove("selected"));
                        btn.classList.add("selected");
                    });
                });
            });
            
            // Clear button
            const clearBtn = document.querySelector(".btn-clear");
            if(clearBtn) {
                clearBtn.addEventListener("click", () => {
                    document.querySelectorAll(".option-btn").forEach(b => b.classList.remove("selected"));
                });
            }
            
            // Quantity buttons
            const qBtns = document.querySelectorAll(".quantity-btn");
            const qInput = document.querySelector(".quantity-input");
            if(qBtns.length === 2 && qInput) {
                qBtns[0].addEventListener("click", () => {
                    let v = parseInt(qInput.value) || 1;
                    if(v > 1) qInput.value = v - 1;
                });
                qBtns[1].addEventListener("click", () => {
                    let v = parseInt(qInput.value) || 1;
                    qInput.value = v + 1;
                });
            }
        });
    </script>
</body>
</html>'''

for p in products:
    content = template.replace('{name}', p['name']).replace('{price}', p['price']).replace('{image}', p['image'])
    with open(p['filename'], 'w', encoding='utf-8') as f:
        f.write(content)

# 📱 J-Intels Calculator - Mobile Access Guide

## Quick Start for Others

Share this information with colleagues or friends to use the calculator:

### **Access URL**
```
http://10.215.191.157:5000
```

### **How to Use on Your Phone:**
1. Make sure you're on the **same WiFi network** as the computer running the server
2. Open **Chrome** (or any browser)
3. Copy and paste the URL above into the address bar
4. Press Enter

### **That's It!**
The professional calculator will load in seconds. No app downloads, no installation.

---

## 💻 **For the Computer Running the Server:**

### **Start the Server:**
```bash
python calculator_web.py
```

### **Access URLs (All work on the same device):**
- **From same computer:** `http://localhost:5000`
- **From same network (phones/tablets):** `http://10.215.191.157:5000`

### **Features Available:**
- ✅ Basic Math: Add, Subtract, Multiply, Divide, Modulus
- ✅ Advanced: Square Root, Trigonometry (sin, cos, tan)
- ✅ Algebra: Solve equations, Differentiate, Integrate
- ✅ Mobile Friendly: Perfect on phones, tablets, computers
- ✅ Fast: Instant results

### **Example Calculations:**
- **Add:** 15 + 25 = 40
- **Algebra:** Solve x² - 4 = (results: -2, 2)
- **Calculus:** Differentiate x² + 3x + 2

---

## ⚠️ **Troubleshooting:**

### **"Cannot reach the address"**
- Check if both devices are on the same WiFi
- Make sure server is running (you should see "Running on http://10.215.191.157:5000")
- Try refreshing the page (Ctrl+R)

### **"Page not loading"**
- Restart the server: Ctrl+C then run `python calculator_web.py` again
- Check Windows Firewall isn't blocking Port 5000
  - Allow Python through Firewall if prompted

### **Different IP Address?**
- Run this command to find your PC's IP:
  ```bash
  ipconfig
  ```
- Look for "IPv4 Address" under your active network connection
- Replace the IP in the URL with your actual IP

---

## 🔒 **Security Note:**

- This setup is for **local network only** (WiFi)
- Not accessible from the internet
- Safe to share the URL with colleagues on your WiFi
- For production use, add authentication and use HTTPS

---

**All set! Share the link and enjoy the calculator!** 🎉

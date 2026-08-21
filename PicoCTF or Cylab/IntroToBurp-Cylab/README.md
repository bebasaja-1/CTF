### WRITE UP
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-21%20073707.png?raw=true)
## Description
Try here to find the flag

## hint
- Try using burpsuite to intercept request to capture the flag.
- Try mangling the request, maybe their server-side code doesn't handle malformed requests very well.

## Solution Steps

### 1. Initial Analysis of the Application
First, I analyzed the web application provided. Upon inspection, 

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-21%20073719.png?raw=true)

I found that a session value was stored by the application.

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-21%20074144.png?raw=true)

### 2. Decoding the Session
I then attempted to decode the text found in the session. As a result, it turned out that the text was encoded using **Base64**. After decoding it, I found a suspicious piece of data:

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-21%20074229.png?raw=true)

### 3. Intercepting with Burp Suite
Next, I switched to using **Burp Suite** to intercept the requests sent by the application. I then proceeded with the registration process, and at that stage, the system required an OTP (One-Time Password) code for 2FA (Two-Factor Authentication) verification.

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-21%20073815.png?raw=true)

### 4. Exploiting the CSRF Token Value as the OTP
Based on the findings from the previous step, I suspected that the previously decoded `csrf_token` value was related to this OTP verification process. I then replaced the `otp` parameter value in the request with the `csrf_token` value using Burp Suite.

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-21%20074344.png?raw=true)

### 5. Result and Flag Retrieval
After sending the request with the modified value, the verification was successfully bypassed, and the flag was found.

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-21%20074337.png?raw=true)




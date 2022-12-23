#!/usr/bin/env python

import os
import sys

# Set up the basic HTML structure
html_str = """
<!DOCTYPE html>
<html>
  <head>
    <style>
      body {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
      }
      .flash {
        animation: flash 1s infinite;
      }
      @keyframes flash {
        50% {
          color: transparent;
        }
      }
      .heart {
        font-size: 3em;
        color: red;
      }
      .present {
        position: absolute;
        bottom: 0;
        right: 0;
        z-index: 1;
      }
      .spotify-track {
        display: none;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
      }
      .banner {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 200px; /* adjust the height of the banner as desired */
        background-image: url("C:/Users/albor/webdev/caroline2.jpg");
        background-size: contain;
      }
      .bottom-banner {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 200px; /* adjust the height of the banner as desired */
        background-image: url("C:/Users/albor/webdev/caroline.jpg");
        background-size: contain;
        z-index: -1;
      }
      .content {
        margin-top: 200px; /* adjust the margin to match the height of the banner */
      }
    </style>
  </head>
  <body>
    <div class="banner"></div>
    <div class="content">
      <div>
        <span class="heart">❤</span>
        <span class="flash">Jeg liker DIG Caroline</span>
        <span class="heart">❤</span>
      </div>
      <img src="C:/Users/albor/webdev/present.png" class="present" onclick="showSpotifyTrack()" alt="Present">
      <div class="spotify-track">
        <iframe src="https://open.spotify.com/embed/track/0D1XO1D1RHuQwQ65yO6YbH" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
      </div>
    </div>
    <div class="bottom-banner"></div>
  </body>
  <script>
    function showSpotifyTrack() {
      document.querySelector('.spotify-track').style.display = 'block';
    }
  </script>
</html>

"""

# Create the HTML file
html_file = open('index.html', 'w', encoding="utf-8")
html_file.write(html_str)
html_file.close()

print('Website generated successfully!')
---
layout: post
title:  "Getting Started"
tags:   updates screenshots
---

Welcome to the very first devblog for the Open Arcade Project!

Like many, I've always loved classic arcade machines, and I've always wanted a machine of my own. In particular, I've always wanted a machine capable of playing multiple games, like Neo Geo systems. However, arcade machines can be _quite_ expensive. There are cheap options out there, of course. There are ways to build machines using emulators, and there are even systems (of questionable legality) preloaded with classic games ready to play for a more reasonable price.

All that said, I'm also a hobbyist game developer. So, I figured why not dive in at the deep end, and make _my own_ arcade machine with multiple games?

Originally, I was planning to do this as a small project, but the more I thought about it, the more I figured: why not share my work? So here we are. All the code for these games will be open source, as will the plans to build the actual machine. The long-term goal will be to offer ready-made packages (or even full OS images) for Raspberry Pi, both for singular games and for the full collection of games, so that anyone can build their own machine, and even contribute to making the games better.

But I'm getting ahead of myself. First thing's first: we need games. Here are the parameters I'll be following as I develop these games:
- Each game should have a native resolution of 640x360, which will scale up to full screen. This will give that nice classic pixel-art look to all of the games, and it's also a resolution that scales up very nicely (i.e. scales by integers) to 720p, 1080p, and beyond.
- Top of the priority list for each game is replay value, as the top cause of machines collecting dust is simply getting bored with the game(s).
- Each game should be playable by one or two players, preferably with the option for the second player to join at any time.
- The machines should support coin operation just in case any arcade owners want to actually set these up like old-school machines, but there should also be an option to just press a button to add credits

Before we can get into any of that, though, we just need _something_ on the screen. So, I present to you the very first screenshot of the Open Arcade Project:

![The first screenshot of Stella Vulpes](/open-arcade-project/img/screenshot.png)

It's... underwhelming. But everything has to start somewhere, and the start I've written is a ship that can fly around the screen and shoot bullets. Don't worry; there's more to come. This first game is tentatively called **Stella Vuples** (bonus points if you catch the reference), and it'll be a classic shoot 'em up. I figure it's best to start with one of the easier styles of game to program.

If you're interested in following the progress of this project, keep an eye on this devblog. I'll be chipping away at the Stella Vulpes engine for a good while. I have ideas for other games as well, but there's no need to get too excited. For now, it's all about building a solid, simple arcade game, making it fun, and building from that foundation.

Until next time,
Josh

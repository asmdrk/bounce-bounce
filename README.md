# bounce-bounce
just a little bouncing ball simulation. Implemented in python and uses pygame for rendering/game physics.

branches:

- main: single ball
- 
- multi-circles: user can press spacebar to spawn 1000 balls at a time. For stress testing. So far I have observed that around 30,000 balls there is some slight slowdown and around 50-60k its quite noticebale
- 
- multi-circles-concurrent (WIP): Plan to implement concurrency via threading or asyncio to evaluate their performance

# Frontier-Navigation
A* Algorithm to find Off-Trial Path

### About the Project

The Skamania II GPS’s off-trail pathfinding feature needs to find the most hiker-friendly trail for an arbitrary terrain. The terrain is represented as a 3D surface discretized into uniformly spaced tiles. The hiker can move with chessboard motion across the XY plane of this surface with the “cost” per step being defined by the change in height for each step:

 $$cost(h0, h1) = e^{h1-h0} = e^{\varDelta h}$$

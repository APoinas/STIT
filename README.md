# Simulation of STIT random tesselations

Simulation of random tesselation **ST**able by **IT**eration introduced by Nagel and Weiss(2015)[[1]](#1). 

## Dependancies

- numpy
- warnings

## Supported distributions for angles

The lines cuting the polygons are defined as
```math
D_{\rho, \theta}=\{(x,y)\in\R^2,~x\cos(\theta)+y\sin(\theta)=\rho\},~\rho\in\R,~\theta\in[0,\pi[.
```
The parameter $\rho$ is always chosen uniformly but various distributions for $\theta$ are supported using the "Dist" parameter.

### Uniform

The default distribution for $\theta$ is the uniform distribution on $[0, \pi]$.

<img src="Example pictures/Example.png" alt="" width="300px"/>

### Side

<img src="Example pictures/Example2.png" alt="" width="300px"/>

### VM

<img src="Example pictures/Example3.png" alt="" width="300px"/>

### Custom

<img src="Example pictures/Example4.png" alt="" width="300px"/>

## References
<a id="1">[1]</a> 
Nagel, Werner, and Viola Weiss. “Crack STIT Tessellations: Characterization of Stationary Random Tessellations Stable with Respect to Iteration.” _Advances in Applied Probability_, vol. 37, no. 4, 2005, pp. 859–83

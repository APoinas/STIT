# Simulation of STIT random tesselations

Simulation of random tesselation **ST**able by **IT**eration introduced by Nagel and Weiss(2015)[[1]](#1). 

## Dependancies

- numpy
- warnings

## Supported distributions for angles

The lines cuting the polygons are defined as
```math
D_{\rho, \theta}=\{(x,y)\in\mathbb{R}^2,~x\cos(\theta)+y\sin(\theta)=\rho\},~\rho\in\mathbb{R},~\theta\in[0,\pi[.
```
The parameter $\rho$ is always chosen uniformly but various distributions for $\theta$ are supported using the "Dist" parameter.

### Uniform

The default distribution for $\theta$ is the uniform distribution on $[0, \pi]$.

<img src="Example pictures/Example.png" alt="" width="300px"/>

### Side

The "Side" distribution correspond to $\mathbb{P}(\theta=\pi/2)=p$ and $\mathbb{P}(\theta=\pi/2)=1-p$ with $p=1/2$ by default. The syntax is
```
STIT(Poly, Stop_Time, Max_iter=500, Dist="Side", p=1/2)
```

<img src="Example pictures/Example2.png" alt="" width="300px"/>

### VM

The "VM" distribution correspond to a Von Mises distribution moudlo $\pi$ with parameters $\mu$ and $\kappa$ that does not have default values and have to be specified. The syntax is
```
STIT(Poly, Stop_Time, Max_iter=500, Dist="VM", mu=None, kappa=None)
```

<img src="Example pictures/Example3.png" alt="" width="300px"/>

### Custom

The "Custom" distribution allows the user to use any custom distribution. A function without parameters returning the random angle has to be specified with the "generator" parameter. The syntax is
```
STIT(Poly, Stop_Time, Max_iter=500, Dist="Custom", generator=None)
```
Here is an example with a $0.3\delta_{\pi/2}+0.7\mathcal{U}([0, \pi[)$ distribution.

<img src="Example pictures/Example4.png" alt="" width="300px"/>

## References
<a id="1">[1]</a> 
Nagel, Werner, and Viola Weiss. “Crack STIT Tessellations: Characterization of Stationary Random Tessellations Stable with Respect to Iteration.” _Advances in Applied Probability_, vol. 37, no. 4, 2005, pp. 859–83

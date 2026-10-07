# A Note on The Lecture by John F. Nash Jr. "An Interesting Equation"

**Author:** Edward J. Zampino  
**Affiliation:** NASA Glenn Research Center  
**Email:** Edward.J.Zampino@nasa.gov  
**Context:** Scholarly working note on John F. Nash Jr.'s 2007 Princeton lecture. Cited as foundational literature for non-equilibrium gravitational stress tensors and Laplace-Beltrami vacuum field formulations in *Epistemic Architectures* (Reference [4] in *The Unified Field*, and field-theoretic correspondence to *Dokument 78*).

> *The ideas presented in this paper are the ideas of the author and are not the scientific opinion or position of any private sector or government organization and are strictly the ideas, hypotheses, and opinions of the author.*

---

## Abstract

The vacuum field equation derived by Professor John F. Nash Jr. containing the Ricci scalar curvature is derived here by using a different Lagrangian density and the form of the Euler-Lagrange equation commonly used in quantum field theory. As an alternative approach to gravity theory, one can use the Yilmaz theory of gravity which avoids theories with fourth-order differential equations.

**Keywords:** $G$-tensor (the Einstein-Hilbert tensor), Ricci tensor, Ricci Scalar Curvature, Lagrangian, Euler-Lagrange equations, Laplace-Beltrami field equation, Energy-Momentum tensor, Divergence-free.

---

## 1. Introduction

In tribute to John F. Nash Jr., the author humbly writes this note about his lecture called *"An interesting equation."* It appears that Dr. Nash was very interested in fourth-order tensor differential equations containing the Einstein-Hilbert tensor and Ricci tensor. He also seemed to be interested in how these field equations might relate to theories of quantum gravity.

In his paper [1], Professor Nash states that his fourth-order covariant-tensor equation is derivable from his choice of a Lagrangian density and the Euler-Lagrange equations. This Lagrangian density is the integrand in the quadruple integral expression on page 1 of his paper (integration over a four-dimensional spacetime region is implied).

---

## 2. Alternate Approach

It was observed that his Lagrangian density in [1] contains the inner product of the Ricci tensor with itself:

$$\mathcal{L} = \sqrt{-g} \left( 2 R_{ab} R^{ab} - R^2 \right)$$

> *(Note: If the signature of the spacetime metric is either $(+ - - -)$ or $(- + + +)$, then the square root $\sqrt{-g}$ can be used instead of the absolute value $\sqrt{|g|}$.)*

That inner product results in a simplification of his Lagrangian. It is reduced to the product of the metric tensor density with the square of the Ricci scalar curvature. The term inside the parentheses becomes:

$$2 R^2 - R^2 = R^2$$

Note that the Lagrangian density is not a function of first-order partial derivatives of the Ricci scalar curvature. So when the resulting Euler-Lagrange equation is calculated, it turns out to be:

$$\sqrt{-g} \, R = 0$$
*(See Appendix A)*

This result implies that the metric tensor collapses to zero or the Ricci scalar curvature is identically zero ($R = 0$).

Now this may be a clue to explore a different choice of Lagrangian density:

$$\mathcal{L} = \frac{1}{2} \sqrt{-g} \, g^{ab} \partial_a R \, \partial_b R - \sqrt{-g} \, U(R)$$

The partial derivatives acting on $R$ imply differentiation performed with respect to spacetime coordinates $\{x^0, x^1, x^2, x^3\}$. The superscripts and subscripts vary from $0$ (time coordinate) to $3$ (the spatial coordinates). We can substitute the above Lagrangian density for $\mathcal{L}$ in the Euler-Lagrange equation and calculate the resulting field equation. 

This type of calculation has been performed for the case of a scalar field $\phi$ with a Minkowski spacetime metric [2]. This approach also works in the case of a general metric tensor.

In the Lagrangian above, $R$ has replaced the scalar field $\phi$. The function $U(R)$ plays the role of a potential and is assumed to be a function of the Ricci scalar curvature. The resulting field equation in terms of $R$ is:

$$\frac{1}{\sqrt{-g}} \partial_a \left( \sqrt{-g} \, g^{ab} \partial_b R \right) = - \frac{\partial U}{\partial R}$$

This equation involves the **Laplace-Beltrami operator** $\Delta$ (left-hand side) and the first-order derivative of the potential with respect to the Ricci scalar curvature (right-hand side). If the potential function $U$ is set equal to zero (the vacuum case), then the field equation equals zero on the right-hand side:

$$\boxed{\Delta R = 0}$$

where $\Delta \equiv \frac{1}{\sqrt{-g}} \partial_a \left( \sqrt{-g} \, g^{ab} \partial_b \right)$ represents the Laplace-Beltrami operator for spacetime (corresponding to the d'Alembertian box symbol $\square$ used by Professor Nash on page 2 of [1]).

---

## 3. The $n$-Dimensional Vacuum Equation

The equation for $\Delta R$ derived by Professor Nash on page 2 of his paper is derived from his fourth-order tensor differential equation for the vacuum:

$$\Delta R + \frac{n-4}{2(n-1)} \left( 2 R_{ab} R^{ab} - R^2 \right) = 0$$

Since he assumed that his fourth-order equations hold for a general $n$-dimensional space, he was able to derive the second term along with $\Delta R$. The parameter $n$ represents the number of dimensions of space-time.

As stated by Prof. Nash, there is a singularity in the differential equation above when $n = 1$ (or $n=2$ depending on the reduction). However, when $n = 4$ (physical four-dimensional spacetime), the prefactor $\frac{4-4}{2(4-1)} = 0$, and the differential equation reduces exactly to:

$$\boxed{\Delta R = 0}$$

Although this result seems like it would be a wave equation and therefore indicate the existence of scalar curvature waves in the vacuum, this cannot be naively assumed. The metric tensors involved with curved space result in complicated Laplace-Beltrami field equations. Even when the resulting partial differential equations may be separable into ordinary differential equations, the radial equations are almost always not solvable in closed form. In the case of the exponential metric, transcendental non-linear equations emerge, so there is no general guarantee that the principle of linear superposition holds.

---

## 4. Alternative Theory: Yilmaz Gravitation

In the case where there is an energy-momentum distribution in space, an alternative theory of gravitation is the **Yilmaz theory**, which avoids the fourth-order partial differential equations studied by Professor Nash. The Yilmaz theory introduces a modification to the Einstein field equations:

$$\frac{1}{2} G_{ab} = T_{ab} + \lambda t_{ab}$$

where the constant $4\pi K / c^4$ is set equal to 1 ($K$ being Newton’s gravitational constant).

* $G_{ab}$ is the Einstein-Hilbert tensor.
* $T_{ab}$ is the stress-energy-momentum tensor of matter.
* $t_{ab}$ is the stress-energy tensor of the gravitational field itself.
* $\lambda$ is a coupling parameter:
  - When $\lambda = 0$, we recover the standard Einstein field equations ($G_{ab} = 2 T_{ab}$).
  - When $\lambda = 1$, we obtain the complete Yilmaz field equations with gravitational field self-stress.

See references [3], [4], and [5]. Subscripts $a, b \in \{0, 1, 2, 3\}$.

---

## Appendix A: Euler-Lagrange Derivation

The Euler-Lagrange equation for a scalar field $R$ is:

$$\frac{\partial \mathcal{L}}{\partial R} - \partial_a \left( \frac{\partial \mathcal{L}}{\partial (\partial_a R)} \right) = 0$$

where $\mathcal{L}$ is the Lagrangian density, and repeated index $a$ implies summation from $a = 0$ to $3$ (Einstein summation convention).

For the simple algebraic Lagrangian:

$$\mathcal{L} = \sqrt{-g} \, R^2$$

The first term yields:

$$\frac{\partial \mathcal{L}}{\partial R} = 2 \sqrt{-g} \, R$$

Because $\mathcal{L}$ is not an explicit function of the coordinate derivatives $\partial_a R$, the second term vanishes identically:

$$\partial_a \left( \frac{\partial \mathcal{L}}{\partial (\partial_a R)} \right) = 0$$

Therefore, the equation of motion is:

$$2 \sqrt{-g} \, R = 0 \implies R \sqrt{-g} = 0$$

This requires that either the Ricci scalar curvature is identically zero ($R = 0$) or the metric determinant collapses ($\sqrt{-g} = 0$).

---

## References

1. **Nash, J. F. Jr. (2007).** *An Interesting Equation.* Lecture delivered February 23, 2007. Files archived at Princeton University Department of Mathematics (converted to LaTeX and PDF by G. Jogesh Babu).
2. **McMahon, D. (2008).** *Quantum Field Theory Demystified.* McGraw-Hill, Chapter 2: "Lagrangian Field Theory," pp. 23, 31 (Euler-Lagrange equations and Klein-Gordon derivation).
3. **Zampino, E. J. (2015/2017).** *Gravitation without Singularities or Event Horizons.* ResearchGate preprint (explanation of the Yilmaz theory of gravitation).
4. **Yilmaz, H. (1992).** *Nuovo Cimento*, 107B, No. 8, pp. 941.
5. **Alley, C. O. (1994).** *Investigations with LASERS, Atomic Clocks and Computer Calculations of Curved Spacetime and the Differences Between the Gravitation Theories of Yilmaz and of Einstein.* In: *Frontiers of Fundamental Physics*, edited by M. Barone and F. Selleri, Plenum Press, New York, p. 132.
6. **Butkov, E. (1968).** *Mathematical Physics.* Addison-Wesley Publishing Co., Section 16.11: "Calculus of Tensors," p. 720 (Laplace-Beltrami operator formulation).
7. **Lancaster, T., & Blundell, S. J. (2014).** *Quantum Field Theory for the Gifted Amateur.* Oxford University Press, Chapter 7, p. 65: "Examples of Lagrangians and how to write down a theory."
8. **McMahon, D. (2008).** *Quantum Field Theory Demystified.* McGraw-Hill, Chapter: "Symmetry Breaking in Field Theory," p. 189.

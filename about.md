---
title: "M-layer project"
hide_sidebar: true
toc: false
permalink: about.html
mathjax: true
last_updated: Nov. 20, 2023
---
The project is coordinated by the NCSLI Measurement Information Infrastructure (MII) technical committee. It is currently led by the Measurement Standards Laboratory of New Zealand ([MSL](https://www.measurement.govt.nz)) with technical support from [Fluke Calibration](https://www.flukecal.com/).

#### The M-layer facilitates data exchange between digital systems
When numerical data is accompanied by a unit (for example, 10.5 N·m) we say that data is *expressed* in terms of the unit (here, a newton-metre).

If a different unit is needed, the numerical factor must be transformed; this transformation will depend on the initial unit and the desired unit. In most cases, we expect a simple conversion factor.

However, unit notation can be ambiguous, which is a problem for digital systems. For instance, 10.5 N·m can be a value of work, or torque; the unit N·m is used to express either quantity. So, it is difficult for a system to determine whether the data can be legitimately expressed in calories, say (another unit of energy).   

The M-layer addresses this problem by defining unique identifiers to accompany numerical data. Pairs of identifiers label the quantity kind and the unit, ensuring there is enough information to identify alternative forms of expression. The M-layer also keeps a register of legitimate transformations between different expressions. 

Data exchange is facilitated by the M-layer. A system will always receive enough information about data to apply legitimate transformations (to preferred forms of expression). Additionally, a receiving system can obtain transformation equations directly from the M-layer, avoiding the need to develop bespoke operations.
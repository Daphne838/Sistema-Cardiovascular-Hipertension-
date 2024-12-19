https://matlab.mathworks.com/open/github/v1?repo=Daphne838/Sistema-Cardiovascular-Hipertension-
[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=Daphne838/Sistema-Cardiovascular-Hipertension-)

# Hipertensión Arterial  

## Estudiantes

Daphne Gamon Aviles; Juana Patricia Rivera Gonzalez; Maria Teresa Gomez Alemon.

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email: 21212156@tectijuana.edu.mx; juana.rivera193@tectijuana.edu.mx ;maria.gomeza17@tectijuana.edu.mx

## Asignaturas o departmento donde se puede usar la Actividad
Modelado de Sistemas Fisiológicos de Ingeniería Biomédica

## Información general
El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivo general
Diseñar un gemelo digital de un sistema fisiológico que permita identificar las diferencias entre un paciente afectado por una enfermedad (caso) y un individuo saludable (control) para desarrollar un protocolo de tratamiento mediante un sistema de control en lazo cerrado.

## Descripción detallada del sistema
El modelo del sistema cardiovascular se representa mediante un circuito eléctrico RLC con dos mallas, en el que los componentes del circuito reflejan las propiedades mecánicas y dinámicas del flujo sanguíneo en las arterias y vasos periféricos. Este enfoque permite una analogía física que facilita el análisis del comportamiento hemodinámico bajo diferentes condiciones fisiológicas y patológicas.

La fuente de voltaje Ve(t) en el modelo simboliza el bombeo del corazón, representando la presión ejercida por el ventrículo izquierdo al expulsar sangre hacia las arterias principales. Por otro lado, la salida de voltaje Vs(t) corresponde a la presión arterial medida en los vasos periféricos, lo que permite evaluar las fluctuaciones de presión a lo largo del sistema.

En términos fisiológicos, cada componente del circuito tiene una interpretación específica:

1. **Inductancia (L)**: Representa la inercia del flujo sanguíneo debido a la masa de la sangre en movimiento. Este parámetro está relacionado con la resistencia al cambio en el flujo, y una disminución en su valor podría interpretarse como una reducción en la capacidad de regulación del flujo por parte del sistema cardiovascular.

2. **Resistencia arterial (R1):** Simboliza la resistencia al flujo sanguíneo en las arterias principales. Este parámetro afecta la cantidad de energía necesaria para impulsar la sangre hacia la periferia.

3. **Resistencia periférica (R2):** Representa la resistencia al flujo sanguíneo en los capilares y pequeños vasos periféricos. Un aumento en R2 se asocia con un mayor esfuerzo que debe realizar el corazón para mantener el flujo, como ocurre en condiciones de hipertensión arterial.

4. **Resistencia a la presión arterial (R3):** Representa la oposición adicional al flujo debido a las condiciones de presión en las arterias principales. Este parámetro es importante para entender los cambios en la presión arterial sistólica y diastólica en diversas patologías cardiovasculares.

5. **Capacitancia (C):** Refleja la elasticidad de las arterias, también conocida como compliance arterial. Este parámetro es crucial para amortiguar las fluctuaciones de presión durante el ciclo cardíaco. Una disminución en la capacitancia indica arterias más rígidas, una condición asociada con arteriosclerosis o envejecimiento.

Este modelo eléctrico RLC es una herramienta útil para estudiar cómo las propiedades del sistema cardiovascular influyen en la presión arterial y el flujo sanguíneo, permitiendo evaluar los efectos de cambios fisiológicos y patológicos como la hipertensión o la disminución de la elasticidad arterial. Además, proporciona una base teórica para diseñar intervenciones clínicas que busquen optimizar el funcionamiento del sistema cardiovascular.



## Referencias principales
[1] PHTLS: Soporte Vital en Trauma Prehospitalario, 10.ª edición, Jones & Bartlett Learning, 2024.

[2] Gómez Pérez, K. C., & D’Alessandro Martínez, A., "Modelos de sistemas fisiológicos: Sistema cardiovascular", Revista de la Facultad de Ingeniería Universidad Central de Venezuela, vol. 21, no. 3, pp. 11-25, 2006.

[3] Regazzoni, F., Salvador, M., Africa, P. C., Fedele, M., Dedè, L., & Quarteroni, A., "A cardiac electromechanics model coupled with a lumped parameters model for closed-loop blood circulation. Part I: model derivation", arXiv preprint arXiv:2011.15040, 2020. 

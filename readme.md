# Taller 2 - Sistema de reservas concurrente

## Problema
Simular un sistema donde 50 usuarios intentan reservar 10 cursos al mismo tiempo.

## Solución sin Lock
- Se muestra la condición de carrera.
- Los asientos pueden llegar a ser negativos.

## Solución con Lock
- Se protege la sección crítica.
- Los asientos nunca son negativos.

## Solución con Semáforo
- Máximo 3 usuarios reservan simultáneamente.
- Se controla el acceso concurrente correctamente.

## Resultados
- Se comprobó la diferencia entre sin Lock, con Lock y con Semáforo.

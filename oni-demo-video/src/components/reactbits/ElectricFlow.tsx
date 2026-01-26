/**
 * ElectricFlow - Flowing electric current lines
 * Tech-inspired, vector aesthetic, calm energy
 */

import React, { useRef, useEffect, useMemo } from 'react';
import { useCurrentFrame, useVideoConfig, interpolate } from 'remotion';

interface FlowLine {
  startY: number;
  amplitude: number;
  frequency: number;
  speed: number;
  phase: number;
  opacity: number;
}

interface ElectricFlowProps {
  lineCount?: number;
  color?: string;
  pulseColor?: string;
  speed?: number;
  showPulses?: boolean;
  pulseCount?: number;
  strokeWidth?: number;
  glowSize?: number;
}

const seededRandom = (seed: number) => {
  const x = Math.sin(seed * 9999) * 10000;
  return x - Math.floor(x);
};

export const ElectricFlow: React.FC<ElectricFlowProps> = ({
  lineCount = 8,
  color = '#0088cc',
  pulseColor = '#00ddff',
  speed = 0.25,
  showPulses = true,
  pulseCount = 3,
  strokeWidth = 2,
  glowSize = 20,
}) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const frame = useCurrentFrame();
  const { width, height, fps } = useVideoConfig();

  // Generate flow lines
  const flowLines = useMemo<FlowLine[]>(() => {
    return Array.from({ length: lineCount }, (_, i) => {
      const progress = i / (lineCount - 1);
      return {
        startY: height * (0.15 + progress * 0.7),
        amplitude: 20 + seededRandom(i * 1.1) * 40,
        frequency: 0.8 + seededRandom(i * 2.2) * 0.6,
        speed: 0.8 + seededRandom(i * 3.3) * 0.4,
        phase: seededRandom(i * 4.4) * Math.PI * 2,
        opacity: 0.4 + seededRandom(i * 5.5) * 0.4,
      };
    });
  }, [lineCount, height]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    ctx.clearRect(0, 0, width, height);

    const time = (frame / fps) * speed;
    const points = 100;

    // Fade in
    const fadeIn = interpolate(frame, [0, 60], [0, 1], {
      extrapolateRight: 'clamp',
    });

    // Draw each flow line
    flowLines.forEach((line, lineIndex) => {
      const lineDelay = lineIndex * 5;
      const lineFade = interpolate(frame - lineDelay, [0, 30], [0, 1], {
        extrapolateLeft: 'clamp',
        extrapolateRight: 'clamp',
      });

      if (lineFade <= 0) return;

      // Calculate path points
      const pathPoints: { x: number; y: number }[] = [];

      for (let i = 0; i <= points; i++) {
        const x = (i / points) * width;
        const xNorm = i / points;

        // Smooth wave
        const wave = Math.sin((xNorm * line.frequency * 2 + time * line.speed + line.phase) * Math.PI * 2);

        // Edge taper
        const edgeTaper = Math.sin(xNorm * Math.PI);

        const y = line.startY + wave * line.amplitude * edgeTaper;

        pathPoints.push({ x, y });
      }

      // Draw main line with glow
      ctx.shadowColor = color;
      ctx.shadowBlur = glowSize * lineFade;

      ctx.beginPath();
      ctx.moveTo(pathPoints[0].x, pathPoints[0].y);

      for (let i = 1; i < pathPoints.length - 1; i++) {
        const xc = (pathPoints[i].x + pathPoints[i + 1].x) / 2;
        const yc = (pathPoints[i].y + pathPoints[i + 1].y) / 2;
        ctx.quadraticCurveTo(pathPoints[i].x, pathPoints[i].y, xc, yc);
      }

      ctx.strokeStyle = color;
      ctx.lineWidth = strokeWidth;
      ctx.lineCap = 'round';
      ctx.globalAlpha = line.opacity * fadeIn * lineFade;
      ctx.stroke();

      // Draw flowing pulses along the line
      if (showPulses && lineFade > 0.5) {
        ctx.shadowBlur = glowSize * 1.5;
        ctx.shadowColor = pulseColor;

        for (let p = 0; p < pulseCount; p++) {
          // Pulse position along line (0 to 1)
          const pulseProgress = ((time * line.speed * 0.5 + p / pulseCount + lineIndex * 0.1) % 1);
          const pulseIndex = Math.floor(pulseProgress * (pathPoints.length - 1));
          const point = pathPoints[pulseIndex];

          if (!point) continue;

          // Pulse intensity (fades at edges)
          const pulseIntensity = Math.sin(pulseProgress * Math.PI);

          // Draw pulse
          const gradient = ctx.createRadialGradient(
            point.x, point.y, 0,
            point.x, point.y, 15
          );
          gradient.addColorStop(0, pulseColor);
          gradient.addColorStop(0.3, `${pulseColor}88`);
          gradient.addColorStop(1, 'transparent');

          ctx.fillStyle = gradient;
          ctx.globalAlpha = pulseIntensity * 0.8 * fadeIn * lineFade;
          ctx.beginPath();
          ctx.arc(point.x, point.y, 15, 0, Math.PI * 2);
          ctx.fill();

          // Bright center
          ctx.fillStyle = '#ffffff';
          ctx.globalAlpha = pulseIntensity * 0.9 * fadeIn * lineFade;
          ctx.beginPath();
          ctx.arc(point.x, point.y, 3, 0, Math.PI * 2);
          ctx.fill();
        }
      }
    });

    // Reset
    ctx.globalAlpha = 1;
    ctx.shadowBlur = 0;

  }, [frame, width, height, fps, flowLines, color, pulseColor, speed, showPulses, pulseCount, strokeWidth, glowSize]);

  return (
    <canvas
      ref={canvasRef}
      width={width}
      height={height}
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
      }}
    />
  );
};

export default ElectricFlow;

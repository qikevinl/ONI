/**
 * FloatingOrbs - Gentle, slow-moving light orbs
 * Creates peaceful, safe atmosphere
 */

import React, { useRef, useEffect, useMemo } from 'react';
import { useCurrentFrame, useVideoConfig, interpolate } from 'remotion';

interface Orb {
  x: number;
  y: number;
  size: number;
  speedX: number;
  speedY: number;
  color: string;
  pulseSpeed: number;
  pulsePhase: number;
}

interface FloatingOrbsProps {
  count?: number;
  colors?: string[];
  minSize?: number;
  maxSize?: number;
  speed?: number;
  blur?: number;
  opacity?: number;
}

const seededRandom = (seed: number) => {
  const x = Math.sin(seed * 9999) * 10000;
  return x - Math.floor(x);
};

export const FloatingOrbs: React.FC<FloatingOrbsProps> = ({
  count = 8,
  colors = ['#0088cc', '#00aadd', '#6688bb', '#4477aa'],
  minSize = 100,
  maxSize = 300,
  speed = 0.1, // Very slow
  blur = 60,
  opacity = 0.25,
}) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const frame = useCurrentFrame();
  const { width, height, fps } = useVideoConfig();

  // Generate orbs once
  const orbs = useMemo<Orb[]>(() => {
    return Array.from({ length: count }, (_, i) => ({
      x: seededRandom(i * 1.1) * width,
      y: seededRandom(i * 2.2) * height,
      size: minSize + seededRandom(i * 3.3) * (maxSize - minSize),
      speedX: (seededRandom(i * 4.4) - 0.5) * speed,
      speedY: (seededRandom(i * 5.5) - 0.5) * speed,
      color: colors[i % colors.length],
      pulseSpeed: 0.02 + seededRandom(i * 6.6) * 0.02,
      pulsePhase: seededRandom(i * 7.7) * Math.PI * 2,
    }));
  }, [count, colors, minSize, maxSize, speed, width, height]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    ctx.clearRect(0, 0, width, height);

    const time = frame / fps;

    // Slow fade in
    const fadeIn = interpolate(frame, [0, 90], [0, 1], {
      extrapolateRight: 'clamp',
    });

    orbs.forEach((orb) => {
      // Gentle floating motion
      const x = orb.x + Math.sin(time * orb.speedX * 10 + orb.pulsePhase) * 50;
      const y = orb.y + Math.cos(time * orb.speedY * 10 + orb.pulsePhase) * 30;

      // Gentle pulse
      const pulse = 0.8 + Math.sin(time * orb.pulseSpeed * 60 + orb.pulsePhase) * 0.2;
      const size = orb.size * pulse;

      // Create soft gradient
      const gradient = ctx.createRadialGradient(x, y, 0, x, y, size);
      gradient.addColorStop(0, `${orb.color}${Math.round(opacity * fadeIn * 255 * 0.5).toString(16).padStart(2, '0')}`);
      gradient.addColorStop(0.4, `${orb.color}${Math.round(opacity * fadeIn * 255 * 0.3).toString(16).padStart(2, '0')}`);
      gradient.addColorStop(1, 'transparent');

      ctx.fillStyle = gradient;
      ctx.beginPath();
      ctx.arc(x, y, size, 0, Math.PI * 2);
      ctx.fill();
    });

  }, [frame, width, height, fps, orbs, opacity]);

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
        filter: `blur(${blur}px)`,
      }}
    />
  );
};

export default FloatingOrbs;

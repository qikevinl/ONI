/**
 * Aurora - Soft, calming aurora borealis effect
 * Gentle gradients that drift slowly - creates safe, relaxed feeling
 */

import React, { useRef, useEffect } from 'react';
import { useCurrentFrame, useVideoConfig, interpolate } from 'remotion';

interface AuroraProps {
  colors?: string[];
  speed?: number;
  blur?: number;
  opacity?: number;
  layers?: number;
}

export const Aurora: React.FC<AuroraProps> = ({
  colors = ['#0066aa', '#0088cc', '#00aadd', '#6633cc', '#4488bb'],
  speed = 0.15, // Very slow for calming effect
  blur = 80,
  opacity = 0.4,
  layers = 4,
}) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const frame = useCurrentFrame();
  const { width, height, fps } = useVideoConfig();

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    ctx.clearRect(0, 0, width, height);

    const time = (frame / fps) * speed;

    // Fade in slowly
    const fadeIn = interpolate(frame, [0, 60], [0, 1], {
      extrapolateRight: 'clamp',
    });

    // Draw aurora layers
    for (let layer = 0; layer < layers; layer++) {
      const layerProgress = layer / layers;
      const color = colors[layer % colors.length];

      // Each layer has different movement pattern
      const xOffset = Math.sin(time * (0.3 + layerProgress * 0.2) + layer) * width * 0.3;
      const yOffset = Math.cos(time * (0.2 + layerProgress * 0.15) + layer * 2) * height * 0.2;

      // Create large elliptical gradient
      const centerX = width * (0.3 + layerProgress * 0.4) + xOffset;
      const centerY = height * (0.2 + layerProgress * 0.3) + yOffset;
      const radiusX = width * (0.4 + Math.sin(time + layer) * 0.1);
      const radiusY = height * (0.3 + Math.cos(time * 0.7 + layer) * 0.1);

      // Draw elliptical gradient
      ctx.save();
      ctx.translate(centerX, centerY);
      ctx.scale(radiusX / radiusY, 1);

      const gradient = ctx.createRadialGradient(0, 0, 0, 0, 0, radiusY);
      gradient.addColorStop(0, `${color}${Math.round(opacity * fadeIn * 255 * 0.6).toString(16).padStart(2, '0')}`);
      gradient.addColorStop(0.5, `${color}${Math.round(opacity * fadeIn * 255 * 0.3).toString(16).padStart(2, '0')}`);
      gradient.addColorStop(1, 'transparent');

      ctx.fillStyle = gradient;
      ctx.beginPath();
      ctx.arc(0, 0, radiusY, 0, Math.PI * 2);
      ctx.fill();

      ctx.restore();
    }

  }, [frame, width, height, fps, colors, speed, blur, opacity, layers]);

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

export default Aurora;

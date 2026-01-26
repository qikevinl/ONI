/**
 * Title Scene - Calm, Relaxed, Safe
 * Slow aurora, gentle orbs, soft threads
 * Designed to evoke trust and tranquility
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';
import { Aurora, FloatingOrbs, Threads, BlurText, GradientText } from '../components/reactbits';
import { colors } from '../data/oni-theme';

export const TitleCalmScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Slower animation phases for calm feeling
  const showONI = frame >= 60;
  const showTagline = frame >= 140;
  const showSubtitle = frame >= 200;

  // Gentle spring animation - more damping for smoother feel
  const oniProgress = spring({
    frame: frame - 60,
    fps,
    config: { damping: 30, stiffness: 30, mass: 2 },
  });

  // Very subtle glow pulse
  const glowPulse = interpolate(
    Math.sin(frame * 0.02), // Slower pulse
    [-1, 1],
    [0.6, 0.9]
  );

  // Gentle scale breathing
  const breathe = interpolate(
    Math.sin(frame * 0.015),
    [-1, 1],
    [0.98, 1.02]
  );

  return (
    <AbsoluteFill
      style={{
        background: 'linear-gradient(180deg, #040810 0%, #0a1525 50%, #081018 100%)',
      }}
    >
      {/* Layer 1: Deep aurora - very slow, soft */}
      <Aurora
        colors={['#0055aa', '#0077bb', '#004488', '#003366']}
        speed={0.08}
        blur={120}
        opacity={0.35}
        layers={3}
      />

      {/* Layer 2: Floating orbs - gentle, peaceful */}
      <FloatingOrbs
        count={6}
        colors={['#0077aa', '#0099bb', '#4477aa', '#3366aa']}
        minSize={150}
        maxSize={400}
        speed={0.05}
        blur={80}
        opacity={0.2}
      />

      {/* Layer 3: Very slow threads - like gentle waves */}
      <div style={{ opacity: 0.25 }}>
        <Threads
          color="#0088bb"
          secondaryColor="#0066aa"
          lineCount={10}
          amplitude={50}
          speed={0.2} // Very slow
          frequency={0.5}
          blur={8}
          opacity={0.4}
        />
      </div>

      {/* Layer 4: Subtle secondary threads */}
      <div style={{ opacity: 0.15 }}>
        <Threads
          color="#4488aa"
          secondaryColor="#3377aa"
          lineCount={6}
          amplitude={30}
          speed={0.15}
          frequency={0.7}
          blur={12}
          opacity={0.3}
        />
      </div>

      {/* Soft vignette for focus */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: `radial-gradient(ellipse at center,
            transparent 0%,
            transparent 30%,
            rgba(4, 8, 16, 0.4) 60%,
            rgba(4, 8, 16, 0.8) 100%
          )`,
          pointerEvents: 'none',
        }}
      />

      {/* Content */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          gap: 28,
        }}
      >
        {/* ONI Logo - gentle fade and scale */}
        {showONI && (
          <div
            style={{
              opacity: Math.max(0, oniProgress),
              transform: `scale(${Math.max(0.8, oniProgress) * breathe})`,
              filter: `drop-shadow(0 0 ${50 * glowPulse}px rgba(0, 136, 204, 0.4))`,
            }}
          >
            <BlurText
              text="ONI"
              delay={60}
              animateBy="letter"
              staggerDelay={15} // Slower stagger
              style={{
                fontSize: 200,
                fontWeight: 700,
                fontFamily: "'Inter', 'Helvetica Neue', sans-serif",
                letterSpacing: '0.02em',
                background: `linear-gradient(180deg,
                  #ffffff 0%,
                  #e0f0ff 30%,
                  #80c0e0 70%,
                  #4090c0 100%
                )`,
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
              }}
            />
          </div>
        )}

        {/* Tagline - soft gradient */}
        {showTagline && (
          <div
            style={{
              opacity: interpolate(frame - 140, [0, 40], [0, 1], { extrapolateRight: 'clamp' }),
              transform: `translateY(${interpolate(frame - 140, [0, 40], [15, 0], { extrapolateRight: 'clamp' })}px)`,
            }}
          >
            <GradientText
              text="Open Neurocomputing Interface"
              delay={140}
              colors={['#4499bb', '#66aacc', '#4499bb']}
              speed={0.2} // Slow gradient movement
              style={{
                fontSize: 24,
                fontWeight: 300,
                letterSpacing: '0.4em',
                textTransform: 'uppercase',
              }}
            />
          </div>
        )}

        {/* Subtitle */}
        {showSubtitle && (
          <div
            style={{
              opacity: interpolate(frame - 200, [0, 50], [0, 1], { extrapolateRight: 'clamp' }),
              transform: `translateY(${interpolate(frame - 200, [0, 50], [10, 0], { extrapolateRight: 'clamp' })}px)`,
            }}
          >
            <span
              style={{
                fontSize: 18,
                fontWeight: 400,
                letterSpacing: '0.2em',
                color: 'rgba(150, 180, 200, 0.8)',
              }}
            >
              The OSI of Mind
            </span>
          </div>
        )}

        {/* Subtle tagline */}
        {frame >= 260 && (
          <div
            style={{
              marginTop: 30,
              opacity: interpolate(frame - 260, [0, 60], [0, 0.6], { extrapolateRight: 'clamp' }),
            }}
          >
            <span
              style={{
                fontSize: 14,
                fontWeight: 400,
                letterSpacing: '0.15em',
                color: 'rgba(100, 150, 180, 0.7)',
              }}
            >
              Protecting what matters most
            </span>
          </div>
        )}
      </div>

      {/* Soft top/bottom gradients */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          height: 200,
          background: 'linear-gradient(rgba(4, 8, 16, 0.6), transparent)',
          pointerEvents: 'none',
        }}
      />
      <div
        style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          right: 0,
          height: 200,
          background: 'linear-gradient(transparent, rgba(4, 8, 16, 0.6))',
          pointerEvents: 'none',
        }}
      />
    </AbsoluteFill>
  );
};

export default TitleCalmScene;

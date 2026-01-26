/**
 * Title Scene - Vector Waves
 * Tech-inspired abstract vector graphics
 * Flows like calm electric water
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';
import { WaveGrid, ElectricFlow, BlurText, GradientText } from '../components/reactbits';
import { colors } from '../data/oni-theme';

export const TitleVectorScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Animation phases
  const showONI = frame >= 50;
  const showTagline = frame >= 120;
  const showSubtitle = frame >= 170;

  // Smooth spring for logo
  const oniProgress = spring({
    frame: frame - 50,
    fps,
    config: { damping: 25, stiffness: 40, mass: 1.5 },
  });

  // Subtle glow pulse
  const glowPulse = interpolate(
    Math.sin(frame * 0.025),
    [-1, 1],
    [0.5, 0.8]
  );

  return (
    <AbsoluteFill
      style={{
        background: 'linear-gradient(180deg, #030508 0%, #050a12 50%, #040810 100%)',
      }}
    >
      {/* Layer 1: Main wave grid - clean vector lines */}
      <WaveGrid
        lineCount={14}
        color="#0077aa"
        secondaryColor="#004466"
        amplitude={35}
        speed={0.2}
        strokeWidth={1.5}
        showNodes={true}
        nodeSize={2.5}
        glow={true}
        glowIntensity={12}
      />

      {/* Layer 2: Electric flow with pulses */}
      <div style={{ opacity: 0.7 }}>
        <ElectricFlow
          lineCount={5}
          color="#005588"
          pulseColor="#00aadd"
          speed={0.15}
          showPulses={true}
          pulseCount={2}
          strokeWidth={1.5}
          glowSize={15}
        />
      </div>

      {/* Layer 3: Subtle background wave grid */}
      <div style={{ opacity: 0.2 }}>
        <WaveGrid
          lineCount={20}
          color="#003355"
          secondaryColor="#002244"
          amplitude={25}
          speed={0.1}
          strokeWidth={1}
          showNodes={false}
          glow={false}
        />
      </div>

      {/* Gradient overlay for depth and readability */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: `radial-gradient(ellipse 80% 60% at 50% 50%,
            rgba(3, 5, 8, 0.3) 0%,
            rgba(3, 5, 8, 0.6) 50%,
            rgba(3, 5, 8, 0.85) 100%
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
          gap: 24,
        }}
      >
        {/* ONI Logo */}
        {showONI && (
          <div
            style={{
              opacity: Math.max(0, oniProgress),
              transform: `scale(${0.9 + Math.max(0, oniProgress) * 0.1})`,
              filter: `drop-shadow(0 0 ${40 * glowPulse}px rgba(0, 119, 170, 0.5))`,
            }}
          >
            <BlurText
              text="ONI"
              delay={50}
              animateBy="letter"
              staggerDelay={12}
              style={{
                fontSize: 180,
                fontWeight: 700,
                fontFamily: "'Inter', 'Helvetica Neue', sans-serif",
                letterSpacing: '0.04em',
                background: `linear-gradient(180deg,
                  #ffffff 0%,
                  #c0e0f0 30%,
                  #60a0c0 70%,
                  #3080a0 100%
                )`,
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
              }}
            />
          </div>
        )}

        {/* Tagline */}
        {showTagline && (
          <div
            style={{
              opacity: interpolate(frame - 120, [0, 35], [0, 1], { extrapolateRight: 'clamp' }),
              transform: `translateY(${interpolate(frame - 120, [0, 35], [12, 0], { extrapolateRight: 'clamp' })}px)`,
            }}
          >
            <GradientText
              text="Open Neurocomputing Interface"
              delay={120}
              colors={['#4090b0', '#60a0c0', '#4090b0']}
              speed={0.15}
              style={{
                fontSize: 22,
                fontWeight: 300,
                letterSpacing: '0.35em',
                textTransform: 'uppercase',
              }}
            />
          </div>
        )}

        {/* Subtitle */}
        {showSubtitle && (
          <div
            style={{
              opacity: interpolate(frame - 170, [0, 40], [0, 1], { extrapolateRight: 'clamp' }),
              transform: `translateY(${interpolate(frame - 170, [0, 40], [10, 0], { extrapolateRight: 'clamp' })}px)`,
              marginTop: 8,
            }}
          >
            <span
              style={{
                fontSize: 16,
                fontWeight: 400,
                letterSpacing: '0.2em',
                color: 'rgba(100, 160, 190, 0.8)',
              }}
            >
              The OSI of Mind
            </span>
          </div>
        )}
      </div>

      {/* Horizontal accent lines */}
      <div
        style={{
          position: 'absolute',
          top: '50%',
          left: 0,
          right: 0,
          height: 1,
          background: `linear-gradient(90deg,
            transparent 0%,
            rgba(0, 119, 170, 0.1) 20%,
            rgba(0, 119, 170, 0.2) 50%,
            rgba(0, 119, 170, 0.1) 80%,
            transparent 100%
          )`,
          transform: 'translateY(-150px)',
          opacity: interpolate(frame, [30, 60], [0, 1], { extrapolateRight: 'clamp' }),
        }}
      />
      <div
        style={{
          position: 'absolute',
          top: '50%',
          left: 0,
          right: 0,
          height: 1,
          background: `linear-gradient(90deg,
            transparent 0%,
            rgba(0, 119, 170, 0.1) 20%,
            rgba(0, 119, 170, 0.2) 50%,
            rgba(0, 119, 170, 0.1) 80%,
            transparent 100%
          )`,
          transform: 'translateY(150px)',
          opacity: interpolate(frame, [30, 60], [0, 1], { extrapolateRight: 'clamp' }),
        }}
      />

      {/* Corner accents */}
      {[
        { top: 60, left: 60 },
        { top: 60, right: 60 },
        { bottom: 60, left: 60 },
        { bottom: 60, right: 60 },
      ].map((pos, i) => (
        <div
          key={i}
          style={{
            position: 'absolute',
            ...pos,
            width: 40,
            height: 40,
            borderTop: pos.top !== undefined ? '1px solid rgba(0, 119, 170, 0.3)' : 'none',
            borderBottom: pos.bottom !== undefined ? '1px solid rgba(0, 119, 170, 0.3)' : 'none',
            borderLeft: pos.left !== undefined ? '1px solid rgba(0, 119, 170, 0.3)' : 'none',
            borderRight: pos.right !== undefined ? '1px solid rgba(0, 119, 170, 0.3)' : 'none',
            opacity: interpolate(frame, [40, 70], [0, 0.6], { extrapolateRight: 'clamp' }),
          }}
        />
      ))}
    </AbsoluteFill>
  );
};

export default TitleVectorScene;

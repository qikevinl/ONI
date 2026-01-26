/**
 * Title Scene - Apple-quality production
 * Smooth, elegant, minimal
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate, Easing } from 'remotion';
import { WaveGrid } from '../components/reactbits';

export const TitleScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Apple-style ease - smooth and deliberate
  const appleEase = (t: number) => {
    // Cubic bezier approximation of Apple's signature ease
    return t < 0.5
      ? 4 * t * t * t
      : 1 - Math.pow(-2 * t + 2, 3) / 2;
  };

  // Slow, elegant fade in for waves
  const waveOpacity = interpolate(frame, [0, 60], [0, 0.6], {
    extrapolateRight: 'clamp',
  });

  // Subtle wave glow - gentle pulse
  const waveGlow = interpolate(
    Math.sin(frame * 0.02),
    [-1, 1],
    [6, 10]
  );

  // ONI reveal - slow and majestic
  const oniRevealRaw = interpolate(frame, [30, 90], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const oniReveal = appleEase(oniRevealRaw);

  // Individual letter staggers - very subtle
  const letterDelays = [0, 8, 16];
  const letterConfigs = ['O', 'N', 'I'].map((letter, i) => {
    const letterRaw = interpolate(frame - 35 - letterDelays[i], [0, 50], [0, 1], {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
    });
    return {
      letter,
      progress: appleEase(letterRaw),
    };
  });

  // Tagline - fades in after ONI settles
  const taglineRaw = interpolate(frame, [100, 140], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const taglineProgress = appleEase(taglineRaw);

  // Subtitle
  const subtitleRaw = interpolate(frame, [130, 170], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const subtitleProgress = appleEase(subtitleRaw);

  // Very subtle glow breathing
  const glowBreath = interpolate(
    Math.sin(frame * 0.025),
    [-1, 1],
    [0.85, 1]
  );

  return (
    <AbsoluteFill
      style={{
        background: '#000000',
      }}
    >
      {/* Subtle radial gradient behind */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: `radial-gradient(ellipse 80% 70% at 50% 50%,
            rgba(0, 40, 60, 0.4) 0%,
            rgba(0, 20, 35, 0.2) 40%,
            transparent 70%
          )`,
          opacity: waveOpacity,
        }}
      />

      {/* Clean wave background - subtle and elegant */}
      <div style={{ opacity: waveOpacity }}>
        <WaveGrid
          lineCount={8}
          color="#0088b0"
          secondaryColor="#006080"
          amplitude={25}
          speed={0.08}
          strokeWidth={1}
          showNodes={false}
          glow={true}
          glowIntensity={waveGlow}
        />
      </div>

      {/* Content */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          gap: 40,
        }}
      >
        {/* ONI Letters */}
        <div
          style={{
            display: 'flex',
            alignItems: 'flex-end',
            justifyContent: 'center',
            filter: `drop-shadow(0 0 ${60 * glowBreath}px rgba(0, 160, 220, 0.35))`,
          }}
        >
          {letterConfigs.map(({ letter, progress }, i) => {
            const y = interpolate(progress, [0, 1], [40, 0]);
            const opacity = progress;
            const scale = interpolate(progress, [0, 1], [0.95, 1]);

            return (
              <div
                key={i}
                style={{
                  position: 'relative',
                  fontSize: 200,
                  fontWeight: 700,
                  fontFamily: "-apple-system, 'SF Pro Display', 'Helvetica Neue', sans-serif",
                  letterSpacing: '0.02em',
                  background: `linear-gradient(180deg,
                    #ffffff 0%,
                    #ffffff 35%,
                    #c0e8f8 55%,
                    #40b8e0 80%,
                    #2090c0 100%
                  )`,
                  WebkitBackgroundClip: 'text',
                  WebkitTextFillColor: 'transparent',
                  backgroundClip: 'text',
                  transform: `translateY(${y}px) scale(${scale})`,
                  opacity,
                }}
              >
                {letter}
                {/* Neural signal inside the O */}
                {letter === 'O' && progress > 0.9 && (() => {
                  const signalOpacity = interpolate(progress, [0.9, 1], [0, 1]);

                  return (
                    <div
                      style={{
                        position: 'absolute',
                        top: '50%',
                        left: '50%',
                        transform: 'translate(-50%, -50%)',
                        width: 80,
                        height: 50,
                        opacity: signalOpacity,
                        overflow: 'hidden',
                      }}
                    >
                      {/* Animated brainwave/EKG line inside O */}
                      <svg width="80" height="50" viewBox="0 0 80 50">
                        <path
                          d={`M 0 25
                              L 15 25
                              L 20 ${25 + Math.sin(frame * 0.15) * 8}
                              L 28 ${25 - Math.sin(frame * 0.15 + 0.5) * 12}
                              L 35 ${25 + Math.cos(frame * 0.12) * 6}
                              L 40 ${15 - Math.abs(Math.sin(frame * 0.1)) * 8}
                              L 45 ${25 - Math.sin(frame * 0.15) * 6}
                              L 52 ${25 + Math.sin(frame * 0.15 + 1) * 10}
                              L 60 ${25 - Math.cos(frame * 0.12) * 5}
                              L 65 25
                              L 80 25`}
                          stroke="#40d8ff"
                          strokeWidth="2.5"
                          fill="none"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          style={{
                            filter: 'drop-shadow(0 0 4px rgba(64, 216, 255, 0.9))',
                          }}
                        />
                        {/* Pulsing dot at peak */}
                        <circle
                          cx="40"
                          cy={15 - Math.abs(Math.sin(frame * 0.1)) * 8}
                          r="3"
                          fill="#ffffff"
                          style={{
                            filter: 'drop-shadow(0 0 6px rgba(100, 220, 255, 1))',
                          }}
                        />
                      </svg>
                    </div>
                  );
                })()}
              </div>
            );
          })}
        </div>

        {/* Tagline */}
        <div
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: 16,
          }}
        >
          <div
            style={{
              fontSize: 24,
              fontWeight: 300,
              letterSpacing: '0.3em',
              color: '#70b8d8',
              textTransform: 'uppercase',
              fontFamily: "-apple-system, 'SF Pro Display', 'Helvetica Neue', sans-serif",
              opacity: taglineProgress,
              transform: `translateY(${interpolate(taglineProgress, [0, 1], [15, 0])}px)`,
            }}
          >
            Open Neurosecurity Interoperability
          </div>
          <div
            style={{
              fontSize: 16,
              fontWeight: 400,
              letterSpacing: '0.08em',
              color: 'rgba(140, 180, 200, 0.9)',
              fontFamily: "-apple-system, 'SF Pro Text', 'Helvetica Neue', sans-serif",
              opacity: subtitleProgress,
              transform: `translateY(${interpolate(subtitleProgress, [0, 1], [10, 0])}px)`,
            }}
          >
            The OSI of Mind
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

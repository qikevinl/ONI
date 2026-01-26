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
                {/* Animated signal pulse on I */}
                {letter === 'I' && progress > 0.9 && (() => {
                  // Signal animation values
                  const pulseY = Math.sin(frame * 0.18) * 12;
                  const pulseScale = 1 + Math.sin(frame * 0.25) * 0.3;
                  const glowIntensity = 0.6 + Math.sin(frame * 0.2) * 0.4;

                  return (
                    <div
                      style={{
                        position: 'absolute',
                        top: -45,
                        left: '50%',
                        transform: 'translateX(-50%)',
                        opacity: interpolate(progress, [0.9, 1], [0, 1]),
                      }}
                    >
                      {/* Vertical pulse line */}
                      <div
                        style={{
                          position: 'absolute',
                          left: '50%',
                          bottom: 0,
                          width: 2,
                          height: 25,
                          background: 'linear-gradient(to top, rgba(64, 216, 255, 0.8), rgba(64, 216, 255, 0.1))',
                          transform: 'translateX(-50%)',
                        }}
                      />
                      {/* Pulsing dot */}
                      <div
                        style={{
                          width: 10,
                          height: 10,
                          borderRadius: '50%',
                          background: '#ffffff',
                          boxShadow: `0 0 ${12 * glowIntensity}px ${6 * glowIntensity}px rgba(64, 216, 255, ${glowIntensity}),
                                      0 0 ${20 * glowIntensity}px ${10 * glowIntensity}px rgba(64, 216, 255, ${glowIntensity * 0.5})`,
                          transform: `translateY(${pulseY}px) scale(${pulseScale})`,
                        }}
                      />
                      {/* Trail effect */}
                      <div
                        style={{
                          position: 'absolute',
                          top: 5,
                          left: '50%',
                          width: 4,
                          height: 15,
                          background: `linear-gradient(to bottom, rgba(64, 216, 255, ${0.6 - pulseY * 0.02}), transparent)`,
                          transform: `translateX(-50%) translateY(${pulseY}px)`,
                          borderRadius: 2,
                        }}
                      />
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

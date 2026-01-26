/**
 * Problem Scene - Apple-quality production
 * Clean, minimal, impactful messaging
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { WaveGrid } from '../components/reactbits';

export const ProblemScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Apple-style ease
  const appleEase = (t: number) => {
    return t < 0.5
      ? 4 * t * t * t
      : 1 - Math.pow(-2 * t + 2, 3) / 2;
  };

  // Phase timing
  const phase1End = 90;    // "BCIs are here"
  const phase2Start = 100;
  const phase2End = 200;   // "Neurosecurity is..."
  const phase3Start = 220;
  const phase3End = 400;   // Problem words
  const phase4Start = 420;
  const phase4End = 520;   // "Until now"
  const phase5Start = 540; // "ONI changes that"

  // Wave opacity - subtle background
  const waveOpacity = interpolate(frame, [0, 40], [0, 0.3], {
    extrapolateRight: 'clamp',
  });

  // Phase 1: "BCIs are here"
  const bciRaw = interpolate(frame, [20, 70], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const bciProgress = appleEase(bciRaw);
  const bciOut = interpolate(frame, [phase1End, phase1End + 30], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Phase 2: "Neurosecurity today is..."
  const neuroRaw = interpolate(frame, [phase2Start, phase2Start + 50], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const neuroProgress = appleEase(neuroRaw);
  const neuroOut = interpolate(frame, [phase2End, phase2End + 20], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Phase 3: Problem words - staggered
  const problemWords = [
    { word: 'Fragmented.', delay: 0 },
    { word: 'Complex.', delay: 35 },
    { word: 'Inaccessible.', delay: 70 },
  ];
  const problemOut = interpolate(frame, [phase3End, phase3End + 20], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Phase 4: "Until now"
  const untilRaw = interpolate(frame, [phase4Start, phase4Start + 50], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const untilProgress = appleEase(untilRaw);
  const untilOut = interpolate(frame, [phase4End, phase4End + 20], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Phase 5: "ONI changes that"
  const oniRaw = interpolate(frame, [phase5Start, phase5Start + 60], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const oniProgress = appleEase(oniRaw);

  return (
    <AbsoluteFill
      style={{
        background: '#000000',
      }}
    >
      {/* Subtle wave background */}
      <div style={{ opacity: waveOpacity * 0.5 }}>
        <WaveGrid
          lineCount={6}
          color="#006688"
          secondaryColor="#004455"
          amplitude={20}
          speed={0.06}
          strokeWidth={0.8}
          showNodes={false}
          glow={true}
          glowIntensity={5}
        />
      </div>

      {/* Subtle center glow */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: `radial-gradient(ellipse 60% 50% at 50% 50%,
            rgba(0, 40, 60, 0.2) 0%,
            transparent 60%
          )`,
        }}
      />

      {/* Phase 1: BCIs are here */}
      {frame < phase2Start && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            gap: 16,
            opacity: bciProgress * bciOut,
            transform: `translateY(${interpolate(bciProgress, [0, 1], [30, 0])}px)`,
          }}
        >
          <div
            style={{
              fontSize: 56,
              fontWeight: 600,
              fontFamily: "-apple-system, 'SF Pro Display', sans-serif",
              color: '#ffffff',
              letterSpacing: '-0.02em',
            }}
          >
            Brain-computer interfaces are here.
          </div>
          <div
            style={{
              fontSize: 20,
              fontWeight: 400,
              fontFamily: "-apple-system, 'SF Pro Text', sans-serif",
              color: 'rgba(140, 180, 200, 0.7)',
              letterSpacing: '0.02em',
              opacity: interpolate(bciProgress, [0.5, 1], [0, 1]),
            }}
          >
            FDA approved. In clinical trials. Shipping to consumers.
          </div>
        </div>
      )}

      {/* Phase 2: Neurosecurity today is... */}
      {frame >= phase2Start && frame < phase3Start && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            opacity: neuroProgress * neuroOut,
            transform: `translateY(${interpolate(neuroProgress, [0, 1], [25, 0])}px)`,
          }}
        >
          <div
            style={{
              fontSize: 48,
              fontWeight: 500,
              fontFamily: "-apple-system, 'SF Pro Display', sans-serif",
              color: 'rgba(180, 200, 220, 0.9)',
              letterSpacing: '-0.01em',
            }}
          >
            Neurosecurity today is...
          </div>
        </div>
      )}

      {/* Phase 3: Problem words */}
      {frame >= phase3Start && frame < phase4Start && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            gap: 24,
            opacity: problemOut,
          }}
        >
          {problemWords.map(({ word, delay }, i) => {
            const wordRaw = interpolate(frame - phase3Start - delay, [0, 40], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            const wordProgress = appleEase(wordRaw);

            return (
              <div
                key={i}
                style={{
                  fontSize: 72,
                  fontWeight: 600,
                  fontFamily: "-apple-system, 'SF Pro Display', sans-serif",
                  color: i === 2 ? '#ff6b6b' : '#ffffff',
                  letterSpacing: '-0.02em',
                  opacity: wordProgress,
                  transform: `translateY(${interpolate(wordProgress, [0, 1], [20, 0])}px)`,
                }}
              >
                {word}
              </div>
            );
          })}
        </div>
      )}

      {/* Phase 4: Until now */}
      {frame >= phase4Start && frame < phase5Start && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            opacity: untilProgress * untilOut,
            transform: `scale(${interpolate(untilProgress, [0, 1], [0.95, 1])})`,
          }}
        >
          <div
            style={{
              fontSize: 80,
              fontWeight: 700,
              fontFamily: "-apple-system, 'SF Pro Display', sans-serif",
              color: '#ffffff',
              letterSpacing: '-0.02em',
            }}
          >
            Until now.
          </div>
        </div>
      )}

      {/* Phase 5: ONI changes that */}
      {frame >= phase5Start && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            gap: 20,
          }}
        >
          <div
            style={{
              fontSize: 28,
              fontWeight: 400,
              fontFamily: "-apple-system, 'SF Pro Display', sans-serif",
              color: 'rgba(100, 180, 220, 0.9)',
              letterSpacing: '0.15em',
              textTransform: 'uppercase',
              opacity: interpolate(oniProgress, [0, 0.5], [0, 1]),
              transform: `translateY(${interpolate(oniProgress, [0, 1], [15, 0])}px)`,
            }}
          >
            Introducing
          </div>
          <div
            style={{
              fontSize: 90,
              fontWeight: 700,
              fontFamily: "-apple-system, 'SF Pro Display', sans-serif",
              background: `linear-gradient(180deg,
                #ffffff 0%,
                #ffffff 40%,
                #60c8e8 70%,
                #2090c0 100%
              )`,
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent',
              backgroundClip: 'text',
              letterSpacing: '0.02em',
              opacity: oniProgress,
              transform: `translateY(${interpolate(oniProgress, [0, 1], [20, 0])}px)`,
              filter: `drop-shadow(0 0 40px rgba(0, 160, 220, ${0.3 * oniProgress}))`,
            }}
          >
            ONI Framework
          </div>
          <div
            style={{
              fontSize: 22,
              fontWeight: 300,
              fontFamily: "-apple-system, 'SF Pro Text', sans-serif",
              color: 'rgba(140, 190, 210, 0.85)',
              letterSpacing: '0.08em',
              opacity: interpolate(oniProgress, [0.5, 1], [0, 1]),
              transform: `translateY(${interpolate(oniProgress, [0.5, 1], [10, 0])}px)`,
            }}
          >
            A unified neurosecurity stack for the next era of computing
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};

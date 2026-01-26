/**
 * Credits Scene - Powerful closing with manifesto
 * Features: Dramatic text reveals, cinematic pacing
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';
import { FloatingParticles } from '../components/Particles';
import { colors } from '../data/oni-theme';

export const CreditsScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Phase timing for the manifesto
  const showMind = frame >= 0;
  const showFuture = frame >= 90;
  const showRules = frame >= 180;
  const showBecause = frame >= 270;
  const showWelcome = frame >= 420;

  // Glow pulse
  const glowPulse = interpolate(
    Math.sin(frame * 0.04),
    [-1, 1],
    [0.5, 1]
  );

  // Manifesto phrases
  const manifestoPhrases = [
    { text: 'Our mind.', delay: 0, show: showMind },
    { text: 'Our future.', delay: 90, show: showFuture },
    { text: 'Our rules.', delay: 180, show: showRules },
  ];

  return (
    <AbsoluteFill
      style={{
        background: colors.gradients.background,
      }}
    >
      {/* Ambient particles */}
      <FloatingParticles
        count={40}
        color={colors.primary.accentPurple}
        speed={0.08}
        minSize={1}
        maxSize={3}
      />

      {/* Background glow */}
      <div
        style={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          width: 800,
          height: 600,
          transform: 'translate(-50%, -50%)',
          background: `radial-gradient(ellipse, ${colors.primary.accentPurple}15 0%, transparent 60%)`,
          filter: 'blur(60px)',
          opacity: glowPulse,
        }}
      />

      {/* Main content */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          height: '100%',
          gap: 0,
        }}
      >
        {/* Manifesto: Our mind. Our future. Our rules. */}
        <div
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: 20,
            marginBottom: 60,
          }}
        >
          {manifestoPhrases.map((phrase, i) => {
            const phraseProgress = spring({
              frame: frame - phrase.delay,
              fps,
              config: { damping: 25, stiffness: 60 },
            });

            const y = interpolate(Math.max(0, phraseProgress), [0, 1], [50, 0]);
            const opacity = Math.max(0, phraseProgress);
            const blur = interpolate(Math.max(0, phraseProgress), [0, 1], [15, 0]);

            // Fade out when next section appears
            const fadeOut = showBecause
              ? interpolate(frame - 270, [0, 60], [1, 0], { extrapolateRight: 'clamp' })
              : 1;

            if (!phrase.show) return null;

            return (
              <div
                key={phrase.text}
                style={{
                  fontSize: 72,
                  fontWeight: 700,
                  letterSpacing: '-0.02em',
                  background: `linear-gradient(180deg, #ffffff 0%, ${colors.primary.accent} 100%)`,
                  WebkitBackgroundClip: 'text',
                  WebkitTextFillColor: 'transparent',
                  transform: `translateY(${y}px)`,
                  opacity: opacity * fadeOut,
                  filter: `blur(${blur}px)`,
                  textAlign: 'center',
                }}
              >
                {phrase.text}
              </div>
            );
          })}
        </div>

        {/* "Because the most important connections..." */}
        {showBecause && !showWelcome && (
          <div
            style={{
              position: 'absolute',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              gap: 20,
            }}
          >
            {(() => {
              const becauseProgress = spring({
                frame: frame - 270,
                fps,
                config: { damping: 30, stiffness: 50 },
              });

              const fadeOut = showWelcome
                ? interpolate(frame - 420, [0, 40], [1, 0], { extrapolateRight: 'clamp' })
                : 1;

              return (
                <div
                  style={{
                    fontSize: 36,
                    fontWeight: 400,
                    color: colors.text.secondary,
                    textAlign: 'center',
                    maxWidth: 900,
                    lineHeight: 1.5,
                    opacity: Math.max(0, becauseProgress) * fadeOut,
                    transform: `translateY(${interpolate(Math.max(0, becauseProgress), [0, 1], [30, 0])}px)`,
                  }}
                >
                  Because the most important connections
                  <br />
                  <span style={{ color: colors.primary.accent, fontWeight: 500 }}>
                    deserve the most thought.
                  </span>
                </div>
              );
            })()}
          </div>
        )}

        {/* "Welcome to the OSI of Mind" - Final reveal */}
        {showWelcome && (
          <div
            style={{
              position: 'absolute',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              gap: 40,
            }}
          >
            {(() => {
              const welcomeProgress = spring({
                frame: frame - 420,
                fps,
                config: { damping: 20, stiffness: 40 },
              });

              const scale = interpolate(Math.max(0, welcomeProgress), [0, 1], [0.9, 1]);
              const blur = interpolate(Math.max(0, welcomeProgress), [0, 1], [20, 0]);

              return (
                <>
                  <div
                    style={{
                      fontSize: 28,
                      fontWeight: 300,
                      letterSpacing: '0.3em',
                      color: colors.text.muted,
                      textTransform: 'uppercase',
                      opacity: Math.max(0, welcomeProgress),
                      transform: `translateY(${interpolate(Math.max(0, welcomeProgress), [0, 1], [20, 0])}px)`,
                    }}
                  >
                    Welcome to
                  </div>

                  <div
                    style={{
                      fontSize: 88,
                      fontWeight: 800,
                      letterSpacing: '-0.02em',
                      background: `linear-gradient(135deg, #ffffff 0%, ${colors.primary.accent} 50%, ${colors.primary.accentPurple} 100%)`,
                      WebkitBackgroundClip: 'text',
                      WebkitTextFillColor: 'transparent',
                      opacity: Math.max(0, welcomeProgress),
                      transform: `scale(${scale})`,
                      filter: `blur(${blur}px) drop-shadow(0 0 ${40 * glowPulse}px ${colors.primary.accent}44)`,
                      textAlign: 'center',
                    }}
                  >
                    The OSI of Mind
                  </div>

                  {/* ONI tagline */}
                  <div
                    style={{
                      fontSize: 18,
                      fontWeight: 400,
                      letterSpacing: '0.1em',
                      color: colors.text.muted,
                      opacity: interpolate(frame - 480, [0, 30], [0, 1], {
                        extrapolateLeft: 'clamp',
                        extrapolateRight: 'clamp',
                      }),
                      textAlign: 'center',
                      maxWidth: 700,
                      lineHeight: 1.6,
                    }}
                  >
                    Open Neurosecurity Interoperability
                  </div>

                  {/* Credits footer */}
                  <div
                    style={{
                      position: 'absolute',
                      bottom: -200,
                      display: 'flex',
                      flexDirection: 'column',
                      alignItems: 'center',
                      gap: 12,
                      opacity: interpolate(frame - 500, [0, 30], [0, 0.7], {
                        extrapolateLeft: 'clamp',
                        extrapolateRight: 'clamp',
                      }),
                    }}
                  >
                    <div style={{ fontSize: 14, color: colors.text.muted }}>
                      Created by <span style={{ color: colors.text.primary }}>Kevin Qi</span>
                    </div>
                    <div style={{ fontSize: 12, color: colors.text.muted }}>
                      Built with Claude Code • Apache 2.0 • 2026
                    </div>
                  </div>
                </>
              );
            })()}
          </div>
        )}
      </div>

      {/* Corner accents */}
      {[
        { top: 40, left: 40 },
        { top: 40, right: 40 },
        { bottom: 40, left: 40 },
        { bottom: 40, right: 40 },
      ].map((pos, i) => (
        <div
          key={i}
          style={{
            position: 'absolute',
            ...pos,
            width: 60,
            height: 60,
            borderTop: pos.top !== undefined ? `1px solid ${colors.primary.accent}22` : 'none',
            borderBottom: pos.bottom !== undefined ? `1px solid ${colors.primary.accent}22` : 'none',
            borderLeft: pos.left !== undefined ? `1px solid ${colors.primary.accent}22` : 'none',
            borderRight: pos.right !== undefined ? `1px solid ${colors.primary.accent}22` : 'none',
            opacity: interpolate(frame, [0, 60], [0, 0.5], { extrapolateRight: 'clamp' }),
          }}
        />
      ))}
    </AbsoluteFill>
  );
};

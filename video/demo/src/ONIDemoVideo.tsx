import { AbsoluteFill, Audio, Sequence, staticFile, interpolate } from "remotion";
import { colors, sceneTimestamps } from "./data/oni-theme";

// Scene components
import { ColdOpenScene } from "./scenes/ColdOpenScene";
import { TitleScene } from "./scenes/TitleScene";
import { ProblemScene } from "./scenes/ProblemScene";
import { LayersScene } from "./scenes/ONILayersAnimation";
import { CoherenceScene } from "./scenes/CoherenceScene";
import { TARAScene } from "./scenes/TARAScene";
import { AcademicScene } from "./scenes/AcademicScene";
import { CTAScene } from "./scenes/CTAScene";
import { CreditsScene } from "./scenes/CreditsScene";

// Persistent components
import { Watermark } from "./components/Watermark";

export const ONIDemoVideo: React.FC = () => {
  const { coldOpen, title, problem, layers, coherence, tara, academic, cta, credits } = sceneTimestamps;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.primary.dark,
        fontFamily: "'Inter', sans-serif",
      }}
    >
      {/* Ambient tech atmosphere - starts immediately, dips 25% at 9s, fades out before narration */}
      <Sequence from={0} durationInFrames={problem.start + 20}>
        <Audio
          src={staticFile("audio/ambient-tech.mp3")}
          volume={(f) => interpolate(
            f,
            [0, 260, 290, problem.start - 70, problem.start + 20],
            [0.35, 0.35, 0.26, 0.26, 0],
            { extrapolateRight: "clamp" }
          )}
        />
      </Sequence>

      {/* Original pulse - deeper, starts first, fades out as smooth pulse takes over */}
      <Sequence from={0} durationInFrames={210}>
        <Audio
          src={staticFile("audio/original-pulse.mp3")}
          volume={(f) => interpolate(
            f,
            [0, 30, 150, 210],
            [0, 0.7, 0.7, 0],
            { extrapolateRight: "clamp" }
          )}
        />
      </Sequence>

      {/* Smooth pulse - crossfades in, dips at 9s with ambient, continues to boot chime */}
      <Sequence from={150} durationInFrames={422 - 150}>
        <Audio
          src={staticFile("audio/curiosity-pulse.mp3")}
          volume={(f) => {
            const duration = 422 - 150;
            // f is relative to sequence start (frame 150)
            // 9s = frame 270, so relative frame = 270 - 150 = 120
            // Dip from 0.8 to 0.6 at 9s, matching ambient dip
            return interpolate(
              f,
              [0, 60, 110, 140, duration - 20, duration],
              [0, 0.8, 0.8, 0.6, 0.6, 0],
              { extrapolateRight: "clamp" }
            );
          }}
        />
      </Sequence>

      {/* Ding tone at 9.11s - perfect 4th interval, sets up the chime */}
      <Sequence from={273}>
        <Audio src={staticFile("audio/ding-tone.mp3")} volume={0.5} />
      </Sequence>

      {/* Second ding tone at ~11s - perfect 5th interval, bridges to boot chime */}
      <Sequence from={330}>
        <Audio src={staticFile("audio/ding-tone-2.mp3")} volume={0.45} />
      </Sequence>

      {/* Boot chime - starts at 14.07s (frame 422), fades in gradually */}
      <Sequence from={422}>
        <Audio
          src={staticFile("audio/boot-chime.mp3")}
          volume={(f) => interpolate(
            f,
            [0, 45],
            [0, 0.6],
            { extrapolateRight: "clamp" }
          )}
        />
      </Sequence>

      {/* Scene 0: Cold Open (0:00-0:08) - NO VOICEOVER, visuals only */}
      <Sequence from={coldOpen.start} durationInFrames={coldOpen.end - coldOpen.start}>
        <ColdOpenScene />
      </Sequence>

      {/* Scene 1: Title (0:08-0:15) - NO VOICEOVER, visuals only */}
      <Sequence from={title.start} durationInFrames={title.end - title.start}>
        <TitleScene />
      </Sequence>

      {/* Scene 2: Problem Statement (0:15-0:40) */}
      <Sequence from={problem.start} durationInFrames={problem.end - problem.start}>
        <ProblemScene />
      </Sequence>

      {/* Problem scene voiceover - single continuous track */}
      {/* Starts at frame 20 when "BCI are here" text first appears */}
      <Sequence from={problem.start + 20}>
        <Audio src={staticFile("audio/vo-problem.mp3")} />
      </Sequence>

      {/* Scene 3: 14-Layer Model (0:40-1:20) */}
      <Sequence from={layers.start} durationInFrames={layers.end - layers.start}>
        <LayersScene />
      </Sequence>
      <Sequence from={layers.start} durationInFrames={layers.end - layers.start}>
        <Audio src={staticFile("audio/vo-layers.mp3")} />
      </Sequence>

      {/* Scene 4: Coherence Metric (1:20-1:50) */}
      <Sequence from={coherence.start} durationInFrames={coherence.end - coherence.start}>
        <CoherenceScene />
      </Sequence>
      <Sequence from={coherence.start} durationInFrames={coherence.end - coherence.start}>
        <Audio src={staticFile("audio/vo-coherence.mp3")} />
      </Sequence>

      {/* Scene 5: TARA Stack (1:50-2:25) */}
      <Sequence from={tara.start} durationInFrames={tara.end - tara.start}>
        <TARAScene />
      </Sequence>
      <Sequence from={tara.start} durationInFrames={tara.end - tara.start}>
        <Audio src={staticFile("audio/vo-tara.mp3")} />
      </Sequence>

      {/* Scene 6: Academic Foundation (2:25-2:50) */}
      <Sequence from={academic.start} durationInFrames={academic.end - academic.start}>
        <AcademicScene />
      </Sequence>
      <Sequence from={academic.start} durationInFrames={academic.end - academic.start}>
        <Audio src={staticFile("audio/vo-academic.mp3")} />
      </Sequence>

      {/* Scene 7: Call to Action (2:50-3:15) */}
      <Sequence from={cta.start} durationInFrames={cta.end - cta.start}>
        <CTAScene />
      </Sequence>
      <Sequence from={cta.start} durationInFrames={cta.end - cta.start}>
        <Audio src={staticFile("audio/vo-cta.mp3")} />
      </Sequence>

      {/* Scene 8: Credits (3:15-3:30) */}
      <Sequence from={credits.start} durationInFrames={credits.end - credits.start}>
        <CreditsScene />
      </Sequence>
      <Sequence from={credits.start} durationInFrames={credits.end - credits.start}>
        <Audio src={staticFile("audio/vo-credits.mp3")} />
        {/* Wind through open door - bright morning, new beginnings */}
        <Audio src={staticFile("audio/wind-door-morning.mp3")} volume={0.5} />
      </Sequence>

      {/* Persistent watermark - © 2026 Kevin Qi • ONI Neural Security Stack™ */}
      <Watermark position="bottom-right" opacity={0.6} fadeInDelay={60} />
    </AbsoluteFill>
  );
};

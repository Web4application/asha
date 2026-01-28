[asha.ai](https://asha.ai/personas/380)
---
```yaml
+----------------+
|  Input Media   |
| (Audio/Video)  |
+--------+-------+
         |
         v
+----------------+
|   Config YAML  |
| (Job/Project)  |
+--------+-------+
         |
         v
+------------------------+
|   MediapiLot Engine    |
|  (Orchestrator/Core)  |
+----------+-------------+
           |
  +--------+---------+--------+
  |                  |        |
  v                  v        v
+------+          +------+ +---------+
| TTS  |          | STT  | | NLP AI |
| (Text->Speech)  |(Audio| | Summar-|
|                  |->Text)| |  ization) |
+------+          +------+ +---------+
   |                  |        |
   v                  v        v
+-----------------------------------+
|       Subtitle/Transcript          |
|   (.srt / .txt / timed captions)   |
+-----------------------------------+
           |
           v
+-----------------+
|  Post-processing |
|  (Sync, Format,  |
|  Effects, Encode)|
+--------+--------+
         |
         v
+----------------+
|  Output Media  |
| (Audio/Video,  |
|  Subtitles)    |
+----------------+
         |
         v
+----------------+
|  Memory/State  |
| (Store project |
|  progress)     |
+----------------+

from moviepy.editor import VideoFileClip

# Путь к вашему видеофайлу
video_file_path = "video.mov"

# Загрузка видеофайла
video_clip = VideoFileClip(video_file_path)

# Путь для сохранения GIF-файла
gif_file_path = "gif.gif"

# Преобразование видео в GIF
video_clip.write_gif(gif_file_path)

# Освободите ресурсы
video_clip.close()
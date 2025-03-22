import argparse
from PIL import Image, ImageSequence

def composite_gif(foreground_path, background_path, output_path):
    # Open the background PNG and ensure it has an alpha channel
    background = Image.open(background_path).convert("RGBA")
    
    # Open the foreground GIF
    fg_gif = Image.open(foreground_path)
    
    # Calculate center offset for the foreground GIF on the background
    bg_width, bg_height = background.size
    fg_width, fg_height = fg_gif.size
    offset = ((bg_width - fg_width) // 2, (bg_height - fg_height) // 2)

    frames = []
    durations = []
    
    # Process each frame in the GIF
    for frame in ImageSequence.Iterator(fg_gif):
        # Convert frame to RGBA to preserve transparency
        frame = frame.convert("RGBA")
        # Create a new composite frame with the background
        composite = background.copy()
        composite.paste(frame, offset, mask=frame)
        frames.append(composite)
        # Get frame duration (default to 100ms if not set)
        durations.append(frame.info.get("duration", 100))
    
    # Save the frames as a new animated GIF
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        disposal=2
    )

def main():
    parser = argparse.ArgumentParser(
        description="Composite a square GIF with a transparent background onto a rectangular PNG background."
    )
    parser.add_argument("foreground_gif", help="Path to the input square GIF (with transparency).")
    parser.add_argument("background_png", help="Path to the rectangular solid color PNG background.")
    parser.add_argument("output_gif", help="Path for the output composite GIF.")
    args = parser.parse_args()

    composite_gif(args.foreground_gif, args.background_png, args.output_gif)

if __name__ == "__main__":
    main()
    # foreground: /Users/mikel/Documents/your_companies/CLUB_CHERUS/logo/liquid-metal-favicon-SOLID-1024x1024.gif
    # background: /Users/mikel/Documents/Projects/GIF-Overlay-Background/images/161515_background.png
    # output gif: /Users/mikel/Documents/Projects/GIF-Overlay-Background/images/liquid-metal-favicon-SOLID-1024x1024-161515_background.gif
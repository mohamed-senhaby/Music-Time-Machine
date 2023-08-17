# Spotify Billboard Hot 100 Playlist Generator

This script allows you to generate a Spotify playlist containing songs from the Billboard Hot 100 chart of a specific year. It scrapes the Billboard Hot 100 chart page for the provided date to extract song titles, searches for these songs on Spotify using the Spotipy library, and adds them to a newly created playlist.

## Getting Started

Follow these instructions to set up and run the playlist generator on your local machine.

### Prerequisites

- Python (version 3.6 or higher)
- Spotipy library (install using `pip install spotipy`)
- Requests library (install using `pip install requests`)
- Beautiful Soup library (install using `pip install beautifulsoup4`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/spotify-playlist-generator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd spotify-playlist-generator
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Open the `generate_playlist.py` file.

2. Replace `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, and `http://example.com` with your actual Spotify developer credentials and redirect URI.

3. Run the script:

   ```bash
   python generate_playlist.py
   ```

4. Enter the desired year in the format YYYY-MM-DD when prompted.

5. The script will create a Spotify playlist named "YYYY Billboard 100" (e.g., "2023 Billboard 100") and add the songs from that year's Billboard Hot 100 chart.

### Important Notes

- Ensure that you have valid Spotify developer credentials and comply with Spotify's terms of use and API guidelines.
- This script requires user authorization via the Spotify OAuth flow.

### Project Structure

- `generate_playlist.py`: The main script that fetches Billboard Hot 100 data, searches for songs on Spotify, and creates the playlist.
- `requirements.txt`: Contains the list of required Python packages.
- `README.md`: This README file providing project information.

### Contributing

Contributions are welcome! If you find any issues or want to add features, feel free to submit a pull request.


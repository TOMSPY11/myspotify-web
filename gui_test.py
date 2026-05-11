import flet as ft
import webbrowser


# ---------------- LINKS ----------------

def open_github(e):
    e.page.launch_url(
        "https://github.com/TOMSPY11/myspotify.py_terminal"
    )


def spotify_dev(e):
    e.page.launch_url(
        "https://developer.spotify.com/dashboard"
    )


# ---------------- BORDER ----------------

def border_all(color="#262626", width=1):
    return ft.Border(
        left=ft.BorderSide(width, color),
        top=ft.BorderSide(width, color),
        right=ft.BorderSide(width, color),
        bottom=ft.BorderSide(width, color),
    )


# ---------------- INFO CARD ----------------

def info_card(title, text):

    return ft.Container(
        bgcolor="#1c1c1c",
        border_radius=24,
        border=border_all(),
        padding=20,
        margin=15,

        content=ft.Column(
            controls=[

                ft.Text(
                    title,
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color="white"
                ),

                ft.Text(
                    text,
                    size=17,
                    color="#8e8e93",
                    selectable=True
                )

            ],
            spacing=10
        )
    )


# ---------------- APP ----------------

def main(page: ft.Page):

    page.title = "MySpotify Terminal"

    page.window.width = 1600
    page.window.height = 900

    page.bgcolor = "#0d0d0d"

    page.theme_mode = ft.ThemeMode.DARK

    page.padding = 0

    # ---------------- SIDEBAR ----------------

    sidebar = ft.Container(
        width=280,
        bgcolor="#111111",
        padding=30,

        content=ft.Column(
            controls=[

                ft.Text(
                    "MySpotify",
                    size=38,
                    weight=ft.FontWeight.BOLD,
                    color="white"
                ),

                ft.Text(
                    "CLI Terminal Project",
                    size=14,
                    color="#8e8e93"
                ),

                ft.Container(height=20),

                ft.Button(
                    "GitHub",
                    on_click=open_github,
                ),

                ft.Button(
                    "Spotify Developer",
                    on_click=spotify_dev,
                ),

            ],
            spacing=15
        )
    )

    # ---------------- HERO ----------------

    hero = ft.Container(
        bgcolor="#161616",
        border_radius=30,
        border=border_all(),
        padding=35,

        content=ft.Column(
            controls=[

                ft.Text(
                    "Spotify CLI for macOS",
                    size=52,
                    weight=ft.FontWeight.BOLD,
                    color="white"
                ),

                ft.Text(
                    "Modern Spotify terminal interface written in Python",
                    size=22,
                    color="#8e8e93"
                ),

                ft.Row(
                    controls=[

                        ft.Button(
                            "Open GitHub",
                            on_click=open_github,
                            bgcolor="#1DB954",
                            color="black"
                        ),

                        ft.Button(
                            "Spotify Dashboard",
                            on_click=spotify_dev,
                            bgcolor="#1c1c1c",
                            color="white"
                        )

                    ],
                    spacing=15
                )

            ],
            spacing=20
        )
    )

    # ---------------- INFO SECTION ----------------

    info_section = ft.Column(
        scroll=ft.ScrollMode.AUTO,
        expand=True,

        controls=[

            ft.Text(
                "About Project",
                size=34,
                weight=ft.FontWeight.BOLD,
                color="white"
            ),

            info_card(
                "What is this?",
                "MySpotify Terminal is a Spotify CLI interface for macOS "
                "that allows you to interact with Spotify directly from terminal."
            ),

            info_card(
                "Features",
                "• Spotify API support\n"
                "• Terminal based workflow\n"
                "• macOS focused UI\n"
                "• Simple developer setup\n"
                "• Lightweight experience"
            ),

            info_card(
                "Setup",
                "1. Install Python requirements\n"
                "2. Create Spotify developer application\n"
                "3. Copy your API credentials\n"
                "4. Run the CLI project"
            ),

            info_card(
                "Update Log",
                "v0.1.1\n"
                "• New modern Flet UI\n"
                "• Added Spotify Developer shortcut\n"
                "• Improved macOS compatibility\n"
                "• Better layout and spacing\n"
                "• Added scrollable information panel"
            ),

            info_card(
                "Credits",
                "Project Creator\n"
                "• TOMSPY11\n\n"

                "Built With\n"
                "• Python\n"
                "• Flet\n"
                "• Spotify Web API"
            ),

            ft.Text(
                "github.com/TOMSPY11/myspotify.py_terminal",
                size=13,
                color="#8e8e93"
            )

        ]
    )

    # ---------------- MAIN ----------------

    main_content = ft.Container(
        expand=True,
        padding=25,

        content=ft.Column(
            controls=[
                hero,
                ft.Container(height=30),
                info_section
            ],
            expand=True
        )
    )

    # ---------------- LAYOUT ----------------

    page.add(
        ft.Row(
            controls=[
                sidebar,
                main_content
            ],
            expand=True
        )
    )


# ---------------- RUN ----------------

ft.app(target=main)

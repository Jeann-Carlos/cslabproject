<div id="top"></div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The ever-increasing demand for security in the cyberspace environment is
always on the lookout for the safest way to browse the internet without fear of
repercussions. As a result, restrictions are always imposed to prevent malicious
agents from gaining access to our systems. Because of the risks involved, drastic
measures are sometimes taken such as blocking all incoming connections to the
network. Despite there being ways to get around these restrictions, on the rare
occasion that you need to access any restricted network from outside (of their local network), current methods require leaving our system somewhat vulnerable.
This research focuses on creating innovative methods for gaining secure access to
these restricted systems while minimizing any potential hazards involved. The
main scope of this project is to allow those in need of reconnaissance of their
private system to be able to do so without fear of exposing themselves or their
systems. Many governmental and commercial enterprises may find it advantageous to be able to open up their network without granting the entire access
to it and/or exposing it to outsiders. Plausible scenarios where our research
could help is in the incorporation of third-party IT/Network management users
or networks that may be located behind many firewalls.This is currently being
accomplished through the usage of VPN and IPv4 traffic redirection but other
methods are planned.
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
Only two  debian based machines are required for ths project: the server machine and the client machine which should be located under the restricted network to penetrate.

*  For the client side a machine under a restricted network preferafily with debian based linux distribution is required, you will also need acess to this programs:
  ```
  curl
  rsync
  enum4linux
  feroxbuster
  gobuster
  impacket-scripts
  nbtscan
  nikto
  nmap
  onesixtyone
  oscanner
  redis-tools
  smbclient
  smbmap
  snmpwalk
  sslscan
  svwar
  tnscmd10g
  whatweb
  wkhtmltopdf
  python
  openvpn
  ```
My recommendation is to use kali linux: https://www.kali.org/get-kali/
* For the server side a local machine is required to function as a vpn and ahub where all the client info will be transfered.

  
## Insatallion

### Pre-prepared ISO:
 
 * Download the ISO for the respective machines:
   1. Link to the server mahcine iso: [https://example.com](https://example.com)
   2. Link to the client mahcine iso: [https://example.com](https://example.com)
 * Clone the project: 
   ```
   git clone https://github.com/Jeann-Carlos/cslabproject.git
   ```
 * Server Side:
   Run the installation script:
   ```
   sudo chmod 755 ./cslabproject/server_workdir/installation_script.sh
   sudo ./cslabproject/server_workdir/installation_script.sh
   ```
   If you dont have a VPN of your own, you can use the openvpn installer:
   ```
   sudo chmod 755 ./cslabproject/server_workdir/openvpn_install.sh
   sudo ./cslabproject/server_workdir/openvpn_install.sh
   ```
 * Cient Side:
   Run the installation script:
   ```
   sudo chmod 755 ./cslabproject/client_workdir/installation_script.sh
   sudo ./cslabproject/client_workdir/installation_script.sh
   ```

   

   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#top">back to top</a>)</p>
### Manual Installation:


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png

# typed: false
# frozen_string_literal: true

class AiCli < Formula
  desc "A cool AI CLI tool"
  
  # 👇 FIX 1: Point to the current, correct GitHub location
  homepage "https://github.com/Codemaster-AR/AI_CLI"
  
  # 👇 FIX 2: Point the download URL to the correct repository
  url "https://github.com/Codemaster-AR/AI_CLI/archive/refs/tags/v0.1.0.tar.gz"
  
  # 👇 ACTION REQUIRED: You must replace this with the new SHA256 after Step 2 below
  sha256 "REPLACE_ME_WITH_THE_NEW_SHA256" 
  
  license "MIT" # Or whatever license you use

  depends_on "python@3.12"

  def install
    # This is a common pattern for Python tools.
    # It creates a virtual environment and installs the tool and its dependencies into it.
    venv = virtualenv_create(libexec, "python3")
    # Assuming your source code contains a setup.py or pyproject.toml
    venv.pip_install_and_link buildpath 
    
    # Note: If your tool is just a single executable file, the install block would be simpler.
  end

  test do
    # This test assumes the correct output is "AI CLI Version 1.5.0", 
    # but the tool version will depend on what is actually in v0.1.0.
    assert_match "AI CLI Version 1.5.0", shell_output("#{bin}/ai-cli version")
  end
end

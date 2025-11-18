# typed: false
# frozen_string_literal: true

class AiCli < Formula
  desc "A cool AI CLI tool"
  include Language::Python::Virtualenv
  
  # 👇 IMPORTANT: Increment the version number
  version "0.1.1" 
  
  homepage "https://github.com/Codemaster-AR/homebrew-ai"
  
  # 👇 IMPORTANT: Update the URL to point to the new tag
  url "https://github.com/Codemaster-AR/homebrew-ai/archive/refs/tags/v0.1.1.tar.gz" 
  
  # 👇 ACTION REQUIRED: This value MUST be replaced with the SHA256 of the v0.1.1 tarball
  sha256 "REPLACE_ME_WITH_THE_NEW_SHA256_FOR_V0_1_1" 
  
  license "MIT"

  depends_on "python@3.12"

  def install
    venv = virtualenv_create(libexec, "python3")
    venv.pip_install_and_link buildpath 
  end

  test do
    # You may also want to update the expected version here if your CLI tool reports 0.1.1
    assert_match "AI CLI Version 1.5.0", shell_output("#{bin}/ai-cli version")
  end
end

Once you've created the `v0.1.1` tag and run `brew install` to get the new `sha256`, you can push the final formula update.

#!/usr/bin/env bash
set -euo pipefail

MODE=""
CLEAN=0
RESET_README=0

for arg in "$@"; do
  case "$arg" in
    --agents) MODE="agents" ;;
    --claude) MODE="claude" ;;
    --both) MODE="both" ;;
    --clean) CLEAN=1 ;;
    --reset-readme) RESET_README=1 ;;
  esac
done

echo "AI-SDLC Skill Setup"
echo "-------------------"

[ -d "skills" ] || {
  echo "Error: skills/ directory not found."
  exit 1
}

create_link () {
  target_dir=$1

  mkdir -p "$target_dir"

  if [ -e "$target_dir/skills" ]; then
    echo "✓ $target_dir/skills already exists"
    return
  fi

  if ln -s ../skills "$target_dir/skills" 2>/dev/null; then
    echo "✓ Symlink created: $target_dir/skills → ../skills"
  else
    cp -r skills "$target_dir/skills"
    echo "✓ Skills copied to $target_dir/skills"
  fi
}

if [ -z "$MODE" ]; then
  echo ""
  echo "Select the tools you want to support:"
  echo ""
  echo "1) .agents"
  echo "2) .claude"
  echo "3) both"
  echo "4) cancel"
  echo ""
  read -p "Selection [1-4]: " choice

  case "$choice" in
    1) MODE="agents" ;;
    2) MODE="claude" ;;
    3) MODE="both" ;;
    *) echo "Cancelled."; exit 0 ;;
  esac
fi

[ "$MODE" = "agents" ] && create_link ".agents"
[ "$MODE" = "claude" ] && create_link ".claude"
[ "$MODE" = "both" ] && create_link ".agents" && create_link ".claude"

echo ""
echo "Setup complete."

reset_readme () {
  if [ "$RESET_README" -eq 0 ]; then
    echo ""
    read -p "Reset README.md? (y/N): " r
    [[ "$r" =~ ^[Yy]$ ]] || return
  fi

  cat > README.md << 'EOF'
# AI-SDLC Project

- Run: `./setup.sh`
- Skills: `skills/`
EOF

  echo "✓ README.md reset"
}

remove_py () {
  dir=$1
  [ -d "$dir" ] || return

  files=$(find "$dir" -name "*.py" -type f)
  [ -z "$files" ] && return

  echo ""
  echo "$files"

  if [ "$CLEAN" -eq 0 ]; then
    read -p "Remove .py files in $dir? (y/N): " r
    [[ "$r" =~ ^[Yy]$ ]] || return
  fi

  find "$dir" -name "*.py" -type f -delete
  echo "✓ cleaned $dir"
}

reset_readme
remove_py "src/app"
remove_py "tests"

echo ""
echo "✓ Done"
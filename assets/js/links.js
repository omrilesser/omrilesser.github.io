<script>
document.addEventListener("DOMContentLoaded", function() {
  var anchors = document.querySelectorAll('a[href]');

  // Open external links in a new tab
  anchors.forEach(function(anchor) {
    if (anchor.hostname !== window.location.hostname) {
      anchor.setAttribute('target', '_blank');
      anchor.setAttribute('rel', 'noopener noreferrer');
    }
  });
});
</script>

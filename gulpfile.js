var gulp = require('gulp');

gulp.task('default', ['copy']);

gulp.task('copy', function() {
    // copy files
    gulp.src(['bower_components/bootstrap/dist/js/bootstrap.min.js', 'bower_components/jquery/dist/jquery.min.js'])
        .pipe(gulp.dest('js/vendor/'));
    gulp.src(['bower_components/bootstrap/dist/css/bootstrap.min.css'])
        .pipe(gulp.dest('css/vendor/'));
    gulp.src(['bower_components/bootstrap/dist/fonts/*.*'])
        .pipe(gulp.dest('css/fonts/'));
});

gulp.task('watch', function(){
    gulp.watch('css/*.css', ['default']);
});
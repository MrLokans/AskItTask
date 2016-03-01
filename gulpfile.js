var gulp = require('gulp');

gulp.task('default', ['copy_css', 'copy_js']);

gulp.task('copy_js', function() {
    // copy files
    gulp.src(['bower_components/bootstrap/dist/js/bootstrap.min.js', 'bower_components/jquery/dist/jquery.min.js'])
        .pipe(gulp.dest('js/vendor/'));
    gulp.src(['bower_components/eonasdan-bootstrap-datetimepicker/build/js/bootstrap-datetimepicker.min.js'])
        .pipe(gulp.dest('js/vendor/'));
    gulp.src(['bower_components/angular-bootstrap/ui-bootstrap.min.js'])
        .pipe(gulp.dest('js/vendor/'));
    gulp.src(['bower_components/angular-bootstrap/ui-bootstrap-tpls.min.js'])
        .pipe(gulp.dest('js/vendor/'));
    gulp.src(['bower_components/moment/min/moment.min.js'])
        .pipe(gulp.dest('js/vendor/'));
    gulp.src(['bower_components/angular/angular.min.js'])
        .pipe(gulp.dest('js/vendor/'));
    gulp.src(['bower_components/angular-messages/angular-messages.min.js'])
        .pipe(gulp.dest('js/vendor/'));
    gulp.src(['bower_components/ng-dialog/js/ngDialog.min.js'])
        .pipe(gulp.dest('js/vendor/'));
});

gulp.task('copy_css', function(){
    gulp.src(['bower_components/ng-dialog/css/ngDialog.min.css'])
        .pipe(gulp.dest('css/vendor/'));
    gulp.src(['bower_components/ng-dialog/css/ngDialog-theme-default.css'])
        .pipe(gulp.dest('css/vendor/'));
    gulp.src(['bower_components/bootstrap/dist/css/bootstrap.min.css'])
        .pipe(gulp.dest('css/vendor/'));
    gulp.src(['bower_components/angular-bootstrap/ui-bootstrap-csp.css'])
        .pipe(gulp.dest('css/vendor/'));
    gulp.src(['bower_components/bootstrap/dist/fonts/*.*'])
        .pipe(gulp.dest('css/fonts/'));
    gulp.src(['bower_components/eonasdan-bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.min.css'])
        .pipe(gulp.dest('css/vendor/'));
});

gulp.task('watch', function(){
    gulp.watch('css/*.css', ['default']);
});
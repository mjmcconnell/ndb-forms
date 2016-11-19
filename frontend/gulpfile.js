'use strict';

var gulp = require('gulp')
var concat = require('gulp-concat')
var uglify = require('gulp-uglify')
var browserify = require('browserify')
var source = require('vinyl-source-stream')

gulp.task('browserify', function() {
    // Grabs the app.js file
    return browserify('./app/scripts/app.js')
        // bundles it and creates a file called main.js
        .bundle()
        .pipe(source('main.js'))
        // saves it the public/js/ directory
        .pipe(gulp.dest('../app/static/js/'));
})

// Bundle the angular material library components into a single vendor file
gulp.task('vendor', function() {
  gulp.src([
    './node_modules/angular/angular.js',
    './node_modules/angular-aria/angular-aria.js',
    './node_modules/angular-animate/angular-animate.js',
    './node_modules/angular-material/angular-material.js'
  ])
    .pipe(concat('vendor.js'))
    .pipe(uglify())
    .pipe(gulp.dest('../app/static/js/'))

  gulp.src('./node_modules/angular-material/angular-material.min.css')
      .pipe(gulp.dest('../app/static/css/'))
});

gulp.task('watch', function() {
    gulp.watch('app/scripts/**/*.js', ['browserify']);
})

gulp.task('build', ['browserify', 'vendor'])
gulp.task('default', ['watch'])

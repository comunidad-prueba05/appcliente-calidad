<script type="application/javascript">
    {% if form.errors %}
        var errors = '';
        {% for field in form %}
            {% for error in field.errors %}
                errors += '{{ error }}\n';
            {% endfor %}
        {% endfor %}
        {% for error in form.non_field_errors %}
            errors += '{{ error }}\n';
        {% endfor %}
        Swal.fire({
            title: 'Error!',
            text: errors,
            icon: 'error'
        });
    {% endif %}

</script>

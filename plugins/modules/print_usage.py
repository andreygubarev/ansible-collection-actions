from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            message=dict(type='str', required=True)
        )
    )

    message = module.params['message']

    # Print the message
    print(message)

    # Return success
    module.exit_json(changed=False, message=message)

if __name__ == '__main__':
    main()
